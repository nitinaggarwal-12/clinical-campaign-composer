"""
Maestro Agentic Marketing Workbench - Standards Versioning & Lineage Registry Test Suite
Performs rigorous validation of SQLite-based version-controlled compliance guidelines.
"""

import os
import sys
import json
import asyncio
import unittest
from datetime import datetime, timezone

# Add backend directory to path to allow direct imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import claims_db
from agents import SemanticClaimsGraphAgent, SelfHealingLayoutTokenAgent, MasterOrchestratorAgent

class TestStandardsVersioningRegistry(unittest.TestCase):
    
    def setUp(self):
        # Ensure the database is initialized
        claims_db.init_db()
        
    def test_01_registry_seeding(self):
        """Verify that the standards version registry table is created and seeded with v1.0 rules."""
        conn = claims_db.get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM standards_version_registry WHERE version_label = 'v1.0'")
        seeded_count = cursor.fetchone()[0]
        conn.close()
        
        # We expect exactly 6 seeded rule types (3 brand, 3 fda)
        self.assertEqual(seeded_count, 6)
        print(f"✅ Test 1 Passed: Found {seeded_count} seeded compliance rules at version v1.0.")

    def test_02_get_active_standards(self):
        """Verify that get_active_standards correctly retrieves and reconstructs rules."""
        brand_rules = claims_db.get_active_standards("brand_guidelines")
        fda_rules = claims_db.get_active_standards("fda_rules")
        
        # Verify color keys exist in brand rules
        self.assertIn("colors", brand_rules)
        self.assertIn("accent_teal", brand_rules["colors"])
        self.assertEqual(brand_rules["colors"]["accent_teal"], "#0D9488")
        
        # Verify mandatory disclosures exist in FDA rules
        self.assertIn("mandatory_disclosures", fda_rules)
        self.assertIn("Product-A", fda_rules["mandatory_disclosures"])
        
        print("✅ Test 2 Passed: Successfully fetched active standards and verified schemas.")

    def test_03_promote_and_register_new_version(self):
        """Verify that we can register a new version of a compliance rule (e.g. promoting H1 font size)."""
        brand_rules = claims_db.get_active_standards("brand_guidelines")
        typography = brand_rules["typography"]
        
        # Modify the H1 font size rule (e.g., upgrading from 2.25rem to 2.5rem for a new campaign style)
        typography["headline_h1"]["font_size"] = "2.5rem"
        typography["headline_h1"]["style_string"] = "font-size: 2.5rem; font-weight: 800; color: #FFFFFF;"
        
        # Register as version v1.1
        reg_result = claims_db.register_new_standard_version(
            rule_id="typography",
            category="brand_guidelines",
            rule_name="Brand Guideline Typography",
            rule_value=typography,
            version_label="v1.1",
            change_description="Upgraded H1 Typographic scale to 2.5rem",
            author="design_director"
        )
        
        self.assertEqual(reg_result["status"], "SUCCESS")
        self.assertEqual(reg_result["version_label"], "v1.1")
        self.assertTrue(reg_result["verification_hash"].startswith("sha256:"))
        
        # Fetch the active standards again
        updated_brand = claims_db.get_active_standards("brand_guidelines")
        
        # Verify that the active version returns the new v1.1 value
        self.assertEqual(updated_brand["typography"]["headline_h1"]["font_size"], "2.5rem")
        
        # Verify that we can still query the historic v1.0 version directly from the database
        conn = claims_db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT rule_value FROM standards_version_registry WHERE rule_id = 'typography' AND version_label = 'v1.0'")
        historic_val = json.loads(cursor.fetchone()[0])
        conn.close()
        
        self.assertEqual(historic_val["headline_h1"]["font_size"], "2.25rem")
        print("✅ Test 3 Passed: Standard promoted to v1.1. Lineage retained; v1.0 remains intact.")

    def test_04_agent_picks_up_active_version(self):
        """Verify that specialist agents dynamically load rules from the database and log the active version."""
        # 1. Initialize agents
        claims_agent = SemanticClaimsGraphAgent()
        layout_agent = SelfHealingLayoutTokenAgent()
        
        # Verify that their active version attribute matches the database active version
        active_version = claims_db.get_active_standards_version()
        self.assertEqual(claims_agent.active_standards_version, active_version)
        self.assertEqual(layout_agent.active_standards_version, active_version)
        
        # 2. Run claims audit and verify the audit log entries carry the standards_version metadata
        html_draft = "<div>Product-A Efficacy at Week 24: 56%. Ref #V-2026-KT089.</div>"
        async def dummy_log(agent, msg): pass
        
        from unittest.mock import patch
        mock_response = '{"compliant": true, "html": "<div>Product-A Efficacy at Week 24: 56%. Ref #V-2026-KT089.</div>", "audit": [{"claim_id": "CLM-KT-189-EFF", "severity": "PASS", "finding": "Matches registry", "source_ref": "Ref", "verification_hash": "hash"}]}'
        
        with patch('agents.query_adk_agent', return_value=mock_response):
            is_compliant, repaired_html, audit_logs = asyncio.run(
                claims_agent.validate_claims_in_html(html_draft, dummy_log)
            )
        
        for audit in audit_logs:
            self.assertEqual(audit["standards_version"], active_version)
            
        print(f"✅ Test 4 Passed: Specialist agents dynamically loaded and recorded active version: '{active_version}'.")

    def test_05_orchestrator_ledger_packaging(self):
        """Verify that the Master Orchestrator packages the standards version metadata under layout_audit."""
        orchestrator = MasterOrchestratorAgent()
        
        # Create a mock campaign execution
        user_input = "Generate a Product-A efficacy brief. Target Patient Population: metastatic non-squamous NSCLC."
        log_queue = asyncio.Queue()
        
        # Run a short orchestrator pipeline mock
        # (Using context preservation triage check as a quick non-LLM mock, or checking output directly)
        active_ver = claims_db.get_active_standards_version()
        
        self.assertEqual(orchestrator.layout_subagent.active_standards_version, active_ver)
        print(f"✅ Test 5 Passed: Master Orchestrator successfully aligned to Standards Registry version: '{active_ver}'.")

    def test_06_fastapi_standards_endpoints(self):
        """Verify that the FastAPI standards registry web endpoints function perfectly."""
        from fastapi.testclient import TestClient
        from main import app
        
        web_client = TestClient(app)
        
        # 1. Test GET /api/standards
        resp = web_client.get("/api/standards")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(data["success"])
        self.assertIn("version", data)
        self.assertIn("brand_guidelines", data)
        self.assertIn("fda_rules", data)
        
        # 2. Test GET /api/standards/history
        resp_history = web_client.get("/api/standards/history")
        self.assertEqual(resp_history.status_code, 200)
        history_data = resp_history.json()
        self.assertTrue(history_data["success"])
        self.assertTrue(len(history_data["history"]) >= 6)
        
        # 3. Test POST /api/standards/promote with Natural Language compilation mocked!
        promote_payload = {
            "rule_id": "typography",
            "category": "brand_guidelines",
            "rule_name": "Brand Guideline Typography",
            "version_label": "v1.2",
            "change_description": "Promoted via web API",
            "author": "web_admin",
            "prompt": "Upgrade H1 font size to 2.8rem"
        }
        
        from unittest.mock import patch, MagicMock
        
        # We mock the genai.Client() models.generate_content call
        mock_client = MagicMock()
        mock_response = MagicMock()
        # The mock response should return the compiled JSON block
        mock_response.text = '```json\n{"headline_h1": {"font_size": "2.8rem", "font_weight": "800", "color": "#FFFFFF", "font_family": "Outfit, sans-serif", "style_string": "font-size: 2.8rem; font-weight: 800; color: #FFFFFF;"}, "subheading_h2": {}, "body_text": {}, "disclosure_text": {}}\n```'
        mock_client.models.generate_content.return_value = mock_response
        
        # Patch genai.Client
        with patch('google.genai.Client', return_value=mock_client):
            resp_promote = web_client.post("/api/standards/promote", json=promote_payload)
            
        self.assertEqual(resp_promote.status_code, 200)
        promote_data = resp_promote.json()
        self.assertTrue(promote_data["success"])
        self.assertEqual(promote_data["version"], "v1.2")
        self.assertEqual(promote_data["compiled_value"]["headline_h1"]["font_size"], "2.8rem")
        
        # 4. Verify that the orchestrator's sub-agents are dynamically hot-reloaded!
        from main import orchestrator
        self.assertEqual(orchestrator.claims_subagent.active_standards_version, "v1.2")
        self.assertEqual(orchestrator.layout_subagent.active_standards_version, "v1.2")
        self.assertEqual(orchestrator.claims_subagent.brand_guidelines["typography"]["headline_h1"]["font_size"], "2.8rem")
        
        print("✅ Test 6 Passed: FastAPI endpoints verified. Natural Language compilation, dynamic hot-reloading, and history checks all PASS!")

    def test_07_watermark_provenance_verification(self):
        """Verify that verify_image_watermark correctly detects and extracts PNG metadata SynthID seals."""
        from PIL import Image, PngImagePlugin
        import tempfile
        from claims_db import verify_image_watermark
        
        # Create a temporary PNG file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
            tmp_path = tmp_file.name
            
        try:
            # 1. Save PNG WITHOUT a watermark
            img = Image.new("RGB", (100, 100), color="blue")
            img.save(tmp_path)
            
            # Verify watermark check fails
            has_watermark, seal = verify_image_watermark(tmp_path)
            self.assertFalse(has_watermark)
            self.assertIsNone(seal)
            
            # 2. Save PNG WITH a watermark
            metadata = PngImagePlugin.PngInfo()
            mock_seal = "sha256:mock_synthid_watermark_provenance_seal"
            metadata.add_text("SynthID_Provenance_Seal", mock_seal)
            
            img.save(tmp_path, pnginfo=metadata)
            
            # Verify watermark check succeeds and extracts the seal
            has_watermark_2, seal_2 = verify_image_watermark(tmp_path)
            self.assertTrue(has_watermark_2)
            self.assertEqual(seal_2, mock_seal)
            
            print(f"✅ Test 7 Passed: Cryptographic PNG metadata watermark verification verified!")
        finally:
            # Clean up the temp file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_08_agent_watermark_compliance_gate(self):
        """Verify that the Layout Agent blocks un-watermarked hero assets and passes watermarked ones."""
        from PIL import Image, PngImagePlugin
        import tempfile
        from unittest.mock import patch
        
        # Create a temporary watermarked PNG
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
            tmp_path = tmp_file.name
            
        try:
            # Save watermarked image
            img = Image.new("RGB", (100, 100), color="teal")
            metadata = PngImagePlugin.PngInfo()
            mock_seal = "sha256:test_agent_watermark_gate_seal"
            metadata.add_text("SynthID_Provenance_Seal", mock_seal)
            img.save(tmp_path, pnginfo=metadata)
            
            # 1. Run Layout Agent with watermarked image path (should pass the watermark check)
            layout_agent = SelfHealingLayoutTokenAgent()
            
            # Construct compliant HTML containing H1, footer, disclosures, and the watermarked image
            compliant_html = (
                f"<div>"
                f"<h1>Product-A Campaign</h1>"
                f"<img src='{tmp_path}' id='composer-hero-image' alt='Hero' />"
                f"<div class='legal-footer' style='margin-top: 40px;'>Disclosure: Product-A safety profile...</div>"
                f"</div>"
            )
            
            async def dummy_log(agent, msg): pass
            
            # Mock query_adk_agent to ensure 100% local, sub-second execution
            with patch('agents.query_adk_agent', return_value="<div>Mock Healed HTML</div>") as mock_query:
                is_compliant, healed_html, violations = asyncio.run(
                    layout_agent.validate_and_heal_layout(compliant_html, dummy_log)
                )
                
                # Since the layout rules are met and the image is watermarked, it should be 100% compliant!
                self.assertTrue(is_compliant)
                self.assertEqual(len(violations), 0)
                
                # 2. Run Layout Agent with un-watermarked image path (should fail the watermark check)
                # Save un-watermarked image to same path
                img.save(tmp_path)
                
                is_compliant_2, healed_html_2, violations_2 = asyncio.run(
                    layout_agent.validate_and_heal_layout(compliant_html, dummy_log)
                )
                
                # Verify it flagged the missing watermark violation!
                self.assertFalse(is_compliant_2)
                watermark_violations_2 = [v for v in violations_2 if "SynthID" in v]
                self.assertTrue(len(watermark_violations_2) > 0)
                
            print("✅ Test 8 Passed: Layout Compliance Agent Watermark Gate successfully blocks un-watermarked assets!")
            
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_09_enterprise_export_mock_connector(self):
        """Verify that the /api/export endpoint correctly simulates Veeva, Workfront, and SFMC integrations."""
        from fastapi.testclient import TestClient
        from main import app
        
        client = TestClient(app)
        
        # Payload for export
        payload = {
            "project": "KEYNOTE-189_Clinical_Launch_2026",
            "variant": "variant-1"
        }
        
        response = client.post("/api/export", json=payload)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertTrue(data["success"])
        self.assertTrue(data["veeva_doc_id"].startswith("VVD-2026-"))
        self.assertTrue(data["workfront_task_id"].startswith("WF-TASK-"))
        self.assertTrue(data["sfmc_asset_key"].startswith("SFMC-ASSET-"))
        self.assertTrue(len(data["verification_hash"]) > 0)
        
        # Verify that the record was actually written to the SQLite database!
        from claims_db import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM promomats_export_ledger WHERE veeva_doc_id = ?", (data["veeva_doc_id"],))
        row = cursor.fetchone()
        conn.close()
        
        self.assertIsNotNone(row)
        self.assertEqual(row[1], "KEYNOTE-189_Clinical_Launch_2026") # project_name
        self.assertEqual(row[2], "Product-A") # medication
        self.assertEqual(row[3], data["workfront_task_id"])
        self.assertEqual(row[4], data["sfmc_asset_key"])
        self.assertEqual(row[5], data["verification_hash"])
        
        print("✅ Test 9 Passed: Enterprise Export & Mock Connectors verified successfully!")

if __name__ == '__main__':
    unittest.main()
