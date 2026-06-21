"""
Maestro Agentic Marketing Workbench - Quality & Integrity Test Suite (Product-A Edition)
Performs rigorous validation of Product-A-grounded multi-agent orchestration.
"""

import os
import sys
import asyncio
import unittest
from unittest.mock import MagicMock, patch

# Add backend directory to path to allow direct imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents import MasterOrchestratorAgent, GatewaySimulator, SemanticClaimsGraphAgent, SelfHealingLayoutTokenAgent

class TestMaestroCoreEngine(unittest.TestCase):
    
    def setUp(self):
        self.orchestrator = MasterOrchestratorAgent()
        
    # =====================================================================
    # 1. GATEWAY RESILIENCY & RETRY LOOP TESTS
    # =====================================================================
    def test_gateway_resilience_success(self):
        """Verify that the Kong AI Gateway simulator executes queries successfully under normal conditions."""
        gateway = GatewaySimulator(drop_probability=0.0, token_fail_probability=0.0)
        
        with patch('agents.query_adk_agent', return_value="Success Response") as mock_query:
            result = asyncio.run(
                gateway.execute_with_resilience("Test_Agent", self.orchestrator.orchestration_agent, "Query text")
            )
            
            self.assertEqual(result, "Success Response")
            mock_query.assert_called_once_with(self.orchestrator.orchestration_agent, "Query text")

    def test_gateway_resilience_retry_and_recover(self):
        """Verify that the gateway retries and successfully recovers after transient drops."""
        gateway = GatewaySimulator(drop_probability=0.1, token_fail_probability=0.0)
        
        with patch('random.random') as mock_random:
            with patch('agents.query_adk_agent', return_value="Recovered Response") as mock_query:
                # First attempt: 0.05 (triggers TimeoutError)
                # Second attempt: 0.5 (succeeds)
                mock_random.side_effect = [0.05, 0.5]
                
                result = asyncio.run(
                    gateway.execute_with_resilience("Test_Agent", self.orchestrator.orchestration_agent, "Query text")
                )
                
                self.assertEqual(result, "Recovered Response")
                self.assertEqual(mock_query.call_count, 1)

    def test_gateway_resilience_fatal_failure_fallback(self):
        """Verify that the gateway raises an error and the sub-agent catches it and falls back gracefully."""
        gateway = GatewaySimulator(drop_probability=1.0, token_fail_probability=0.0)
        
        from agents import L3StrategyIngestionAgent
        ingestion_agent = L3StrategyIngestionAgent(gateway)
        
        async def dummy_log(agent, msg): pass
        
        result = asyncio.run(
            ingestion_agent.parse_brief("Generate a brand new campaign.", dummy_log)
        )
        
        # Verify the fallback brief is active and grounded in Product-A
        self.assertEqual(result["Campaign Name"], "Product-A First-Line NSCLC Acceleration")
        self.assertEqual(result["Therapeutic Area"], "Oncology")
        self.assertEqual(result["Key Efficacy Claim"], "Product-A (compound_alpha) Efficacy: 56% Overall Response Rate (ORR) at Week 24 (KEYNOTE-189 study)")


    # =====================================================================
    # 2. CONVERSATIONAL TRIAGE (ANTI-LAZY) TESTS
    # =====================================================================
    def test_conversational_triage_vague_prompt(self):
        """Verify that the orchestrator intercepts vague prompts and initiates a conversational triage path."""
        vague_prompt = "fix it"
        log_queue = asyncio.Queue()
        
        result = asyncio.run(
            self.orchestrator.run_orchestrated_pipeline(vague_prompt, log_queue)
        )
        
        # Verify it entered the TRIAGE state instead of failing
        self.assertEqual(result["status"], "TRIAGE")
        self.assertIn("triage", result["message"].lower())
        self.assertIn("vague", result["message"].lower())
        self.assertIn("Campaign Name", result["missing_fields"])
        self.assertEqual(result["last_active_brief"], {})

    def test_conversational_triage_with_history(self):
        """Verify that triage options adapt contextually when there is active session history."""
        mock_brief = {
            "Campaign Name": "Product-A First-Line NSCLC Acceleration",
            "Therapeutic Area": "Oncology",
            "Key Efficacy Claim": "Product-A (compound_alpha) Efficacy: 56% ORR at Week 24 (KEYNOTE-189 study)"
        }
        self.orchestrator.state_history.append(mock_brief)
        
        vague_prompt = "update"
        log_queue = asyncio.Queue()
        
        result = asyncio.run(
            self.orchestrator.run_orchestrated_pipeline(vague_prompt, log_queue)
        )
        
        self.assertEqual(result["status"], "TRIAGE")
        self.assertIn("triage", result["message"].lower())
        self.assertIn("Product-A First-Line NSCLC Acceleration", result["message"])
        self.assertEqual(result["last_active_brief"], mock_brief)


    # =====================================================================
    # 3. CONTEXT PRESERVATION LOOP TESTS
    # =====================================================================
    def test_context_preservation_loop(self):
        """Verify that incremental modifications preserve all other brand constraints (Context Preservation)."""
        initial_brief = {
            "Campaign Name": "Product-A First-Line NSCLC Acceleration",
            "Therapeutic Area": "Oncology",
            "Target Patient Population": "Adults with metastatic non-squamous NSCLC",
            "Key Efficacy Claim": "Product-A (compound_alpha) Efficacy: 56% Overall Response Rate (ORR) at Week 24 (KEYNOTE-189 study)",
            "Key Safety Parameter": "Product-A Safety Profile: 10% Grade 3/4 Immune-Mediated Adverse Reactions",
            "Core Marketing Hook": "Redefining overall survival boundaries with Product-A."
        }
        self.orchestrator.state_history.append(initial_brief)
        
        modification_prompt = "Modify the efficacy rate to 61%"
        log_queue = asyncio.Queue()
        
        with patch('agents.query_adk_agent', return_value="```html\n<div>Draft HTML</div>\n```") as mock_query:
            result = asyncio.run(
                self.orchestrator.run_orchestrated_pipeline(modification_prompt, log_queue)
            )
            
        # Verify that the new brief preserves all original fields, modifying only the efficacy claim
        new_brief = result["brief"]
        self.assertEqual(new_brief["Campaign Name"], "Product-A First-Line NSCLC Acceleration")
        self.assertEqual(new_brief["Therapeutic Area"], "Oncology")
        self.assertEqual(new_brief["Target Patient Population"], "Adults with metastatic non-squamous NSCLC")
        self.assertEqual(new_brief["Key Safety Parameter"], "Product-A Safety Profile: 10% Grade 3/4 Immune-Mediated Adverse Reactions")
        self.assertEqual(new_brief["Core Marketing Hook"], "Redefining overall survival boundaries with Product-A.")
        self.assertEqual(new_brief["Key Efficacy Claim"], "Product-A (compound_alpha) Efficacy: 61% Overall Response Rate (ORR) at Week 24 (KEYNOTE-189 study)")


    # =====================================================================
    # 4. REGULATORY PRECEDENT ENGINE & MOCK DB TESTS
    # =====================================================================
    def test_claims_graph_validation_and_auto_repair(self):
        """Verify that the claims graph agent validates claims against MaterialReview and auto-repairs outdated copy."""
        claims_agent = SemanticClaimsGraphAgent()
        
        # Webhook updates database efficacy parameter to 61% at Week 48
        sync_payload = claims_agent.update_efficacy_label_webhooks("61%", "Week 48")
        self.assertEqual(sync_payload["new_value"], "61%")
        
        outdated_html = "<div>Product-A Efficacy at Week 24: 56%. Reference #V-2026-KT089.</div>"
        async def dummy_log(agent, msg): pass
        
        is_compliant, repaired_html, audit_logs = asyncio.run(
            claims_agent.validate_claims_in_html(outdated_html, dummy_log)
        )
        
        # Verify violation detection and auto-repair
        self.assertFalse(is_compliant)
        self.assertIn("61%", repaired_html)
        self.assertIn("Week 48", repaired_html)
        self.assertNotIn("56%", repaired_html)
        
        # Verify grounded validation metadata
        self.assertEqual(audit_logs[0]["claim_id"], "CLM-KT-189-EFF")
        self.assertEqual(audit_logs[0]["severity"], "CRITICAL")
        self.assertEqual(audit_logs[0]["source_ref"], "Regulatory Compliance Vault Ref #V-2026-KT089")
        self.assertIn("sha256:", audit_logs[0]["verification_hash"])


    # =====================================================================
    # 5. SELF-HEALING LAYOUT TOKEN TESTS
    # =====================================================================
    def test_layout_token_programmatic_fallback_repair(self):
        """Verify that the layout agent programmatically heals HTML if design tokens are violated."""
        gateway = GatewaySimulator(drop_probability=1.0)
        layout_agent = SelfHealingLayoutTokenAgent(gateway)
        
        violating_html = "<div>Standard text headline. Under 60 population.</div>"
        async def dummy_log(agent, msg): pass
        
        is_compliant, healed_html, violations = asyncio.run(
            layout_agent.validate_and_heal_layout(violating_html, dummy_log)
        )
        
        # Verify it flagged the layout and programmatically healed it
        self.assertFalse(is_compliant)
        self.assertIn("h1", healed_html.lower())
        self.assertIn("legal-footer", healed_html.lower())
        self.assertIn("Regulatory Compliance Vault Ref #V-2026-KTS99", healed_html)

if __name__ == '__main__':
    unittest.main()
