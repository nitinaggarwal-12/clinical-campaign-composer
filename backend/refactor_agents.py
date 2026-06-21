import os
import re

def refactor_agents():
    agents_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agents.py")
    
    with open(agents_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # =====================================================================
    # NEW SEMANTIC CLAIMS GRAPH AGENT (Wrapped in triple single quotes)
    # =====================================================================
    new_claims_agent_code = '''class SemanticClaimsGraphAgent:
    def __init__(self, gateway: GatewaySimulator, model_name: str = "gemini-2.5-flash"):
        self.gateway = gateway
        self.agent = LlmAgent(
            name="Semantic_Claims_Graph_Agent",
            model=model_name,
            description="Cross-references marketing copy against the active MaterialReview claims registry.",
            instruction="""
            You are the Semantic Claims Graph Agent. Your job is to verify that all medical, efficacy, and safety claims made in the marketing HTML copy match the active Regulatory Compliance Vault registry EXACTLY.
            
            You will be provided with:
            1. The current active Regulatory Compliance Vault claims registry database (grounded truth).
            2. The draft HTML copy.
            
            Your tasks:
            1. Scan the HTML for any efficacy claims (e.g. Overall Response Rate, ORR %, Objective Response Rate) and safety claims (e.g. Adverse Events, Grade 3/4 AEs %).
            2. Cross-reference them against the active values in the registry.
            3. If the HTML copy contains outdated or incorrect numbers relative to the registry, you must identify the violation, flag it as CRITICAL, and rewrite the HTML to synchronize it with the active registry value.
            4. If the HTML copy matches the registry, flag it as a PASS.
            5. Generate a structured JSON audit log containing the results:
               [
                 {
                   "claim_id": "ComplianceVault claim ID",
                   "severity": "PASS" or "CRITICAL",
                   "finding": "Detailed description of the finding, citing the exact numbers.",
                   "recommendation": "What should be changed, or 'None' if compliant.",
                   "source_ref": "ComplianceVault reference code",
                   "verification_hash": "SHA-256 seal from the database",
                   "action": "AUTO-REPAIR TRIGGERED" or "None"
                 }
               ]
            
            Return a JSON object containing exactly three fields:
            - "compliant": true or false
            - "html": "The final validated (and repaired, if necessary) HTML copy. Keep all layout elements intact."
            - "audit": [ The list of audit log objects ]
            
            Return ONLY a valid JSON block, with no markdown formatting or conversational text outside.
            """
        )
        
        # Relational Claims Graph - Grounded in Regulatory Compliance Vault registries for Global Pharma products
        self.material_review_db = {
            "product_a_efficacy": {
                "claim_id": "CLM-KT-189-EFF",
                "trial_record": "KEYNOTE-189 Phase III Trial (NCT02578680)",
                "parameter": "Overall Response Rate (ORR)",
                "value_at_week_24": "56%",
                "value_at_week_48": "61%",
                "active_version": "Week 24", 
                "current_efficacy_value": "56%",
                "source_ref": "Regulatory Compliance Vault Ref #V-2026-KT089",
                "verification_hash": "sha256:d8b02ea9a11c8e5d2b71a3f009a1c662863a9b11c8e5d2b71a3f009a1c66286",
                "last_updated": "2026-01-10T10:00:00Z"
            },
            "product_a_safety": {
                "claim_id": "CLM-KT-189-SAF",
                "trial_record": "KEYNOTE-189 Immune-Mediated Adverse Reactions (NCT02578680)",
                "parameter": "Grade 3/4 Immune-Mediated Adverse Reactions",
                "value": "10%",
                "active_version": "v2.1",
                "source_ref": "Regulatory Compliance Vault Ref #V-2026-KTS99",
                "verification_hash": "sha256:8f9c2eb3a901c4e5d2b71a3f009a1c77f00a2eb3a901c77f00a2eb3a901c66",
                "last_updated": "2026-02-15T08:30:00Z"
            }
        }

    def update_efficacy_label_webhooks(self, new_value: str, active_version: str = "Week 48") -> Dict[str, Any]:
        old_val = self.material_review_db["product_a_efficacy"]["current_efficacy_value"]
        self.material_review_db["product_a_efficacy"]["active_version"] = active_version
        self.material_review_db["product_a_efficacy"]["current_efficacy_value"] = new_value
        self.material_review_db["product_a_efficacy"]["last_updated"] = "2026-06-15T22:26:00Z"
        new_hash = f"sha256:f52d9a3b84c8e77a012b{random.randint(1000, 9999)}c2eb3a901c4e5d2b71a3f"
        self.material_review_db["product_a_efficacy"]["verification_hash"] = new_hash
        
        return {
            "status": "SUCCESS",
            "claim_id": "CLM-KT-189-EFF",
            "parameter": "Overall Response Rate (ORR)",
            "old_value": old_val,
            "new_value": new_value,
            "active_version": active_version,
            "verification_hash": new_hash,
            "compliance_vault_material_review_sync": "COMPLETED",
            "timestamp": "2026-06-15T22:26:00Z"
        }

    async def validate_claims_in_html(self, html_content: str, log_callback) -> Tuple[bool, str, List[Dict[str, Any]]]:
        await log_callback("Semantic_Claims_Graph_Agent", "Accessing Regulatory Compliance Vault claims ledger...")
        await asyncio.sleep(0.4)
        
        prompt = f\"\"\"
        MaterialReview Claims Registry:
        {json.dumps(self.material_review_db, indent=2)}
        
        Marketing HTML Copy Draft:
        {html_content}
        \"\"\"
        
        try:
            response = await self.gateway.execute_with_resilience(
                "Semantic_Claims_Graph_Agent",
                self.agent,
                prompt
            )
            
            cleaned_response = response.strip()
            if "```json" in cleaned_response:
                cleaned_response = cleaned_response.split("```json")[1].split("```")[0].strip()
            elif "```" in cleaned_response:
                cleaned_response = cleaned_response.split("```")[1].split("```")[0].strip()
                
            result = json.loads(cleaned_response)
            is_compliant = result.get("compliant", True)
            modified_html = result.get("html", html_content)
            audit_logs = result.get("audit", [])
            
            for audit in audit_logs:
                if audit.get("severity") == "CRITICAL":
                    await log_callback("Semantic_Claims_Graph_Agent", f"⚠️ CRITICAL CLAIM VIOLATION: {audit.get('finding')}")
                    await log_callback("Semantic_Claims_Graph_Agent", f"🔧 AUTO-REPAIR: {audit.get('recommendation')} - Cryptographic Lock: {audit.get('verification_hash')}")
                else:
                    await log_callback("Semantic_Claims_Graph_Agent", f"✅ CLAIM COMPLIANCE: {audit.get('finding')}")
                    
            return is_compliant, modified_html, audit_logs
            
        except Exception as e:
            await log_callback("Semantic_Claims_Graph_Agent", f"⚠️ Claims Graph AI unavailable ({str(e)}). Deploying dynamic, drug-aware regex engine...")
            return self.local_regex_fallback(html_content, log_callback)

    def local_regex_fallback(self, html_content: str, log_callback) -> Tuple[bool, str, List[Dict[str, Any]]]:
        audit_logs = []
        is_compliant = True
        modified_html = html_content

        efficacy_data = self.material_review_db.get("product_a_efficacy", {})
        safety_data = self.material_review_db.get("product_a_safety", {})
        
        active_efficacy = efficacy_data.get("current_efficacy_value", "56%")
        active_version = efficacy_data.get("active_version", "v1.0")
        efficacy_hash = efficacy_data.get("verification_hash", "sha256:d8b")
        efficacy_ref = efficacy_data.get("source_ref", "ComplianceVault Ref")
        
        # Check efficacy in HTML
        efficacy_pct = active_efficacy.replace("%", "").strip()
        if efficacy_pct not in html_content:
            matches = re.findall(r'(\\d+)\\s*%', html_content)
            if matches:
                is_compliant = False
                audit_logs.append({
                    "claim_id": efficacy_data.get("claim_id", "CLM-EFF"),
                    "severity": "CRITICAL",
                    "finding": f"Outdated claim detected! HTML contains '{matches[0]}%' ORR, but active registry is '{active_efficacy}' ({active_version}).",
                    "recommendation": f"Update efficacy parameter to '{active_efficacy}' and reference '{active_version}' clinical outcomes.",
                    "source_ref": efficacy_ref,
                    "verification_hash": efficacy_hash,
                    "action": "AUTO-REPAIR TRIGGERED"
                })
                modified_html = re.sub(rf'{matches[0]}\\s*%', active_efficacy, modified_html)
                modified_html = re.sub(r'Week \\d+|v\\d+\\.\\d+', active_version, modified_html)
        else:
            audit_logs.append({
                "claim_id": efficacy_data.get("claim_id", "CLM-EFF"),
                "severity": "PASS",
                "finding": f"Efficacy claim matches active MaterialReview value of '{active_efficacy}' ({active_version}).",
                "source_ref": efficacy_ref,
                "verification_hash": efficacy_hash,
                "recommendation": "None. Claim is fully grounded and compliant."
            })
            
        # Check safety in HTML
        active_safety = safety_data.get("value", "10%")
        safety_hash = safety_data.get("verification_hash", "sha256:8f")
        safety_ref = safety_data.get("source_ref", "ComplianceVault Ref")
        
        safety_pct = active_safety.replace("%", "").strip()
        if safety_pct not in html_content:
            matches = re.findall(r'(\\d+)\\s*%\\s*(?:grade|adverse|safety|reactions|immune)', html_content.lower())
            if matches:
                is_compliant = False
                audit_logs.append({
                    "claim_id": safety_data.get("claim_id", "CLM-SAF"),
                    "severity": "CRITICAL",
                    "finding": f"Safety claim mismatch! HTML contains incorrect safety percentage, but active record is '{active_safety}'.",
                    "recommendation": f"Update safety parameter to '{active_safety}' adverse reactions.",
                    "source_ref": safety_ref,
                    "verification_hash": safety_hash,
                    "action": "AUTO-REPAIR TRIGGERED"
                })
                modified_html = re.sub(rf'{matches[0]}\\s*%', active_safety, modified_html)
        else:
            audit_logs.append({
                "claim_id": safety_data.get("claim_id", "CLM-SAF"),
                "severity": "PASS",
                "finding": f"Safety claim matches active MaterialReview record of '{active_safety}'.",
                "source_ref": safety_ref,
                "verification_hash": safety_hash,
                "recommendation": "None. Claim is fully compliant."
            })
            
        return is_compliant, modified_html, audit_logs'''

    # =====================================================================
    # NEW SELF-HEALING LAYOUT TOKEN AGENT (Wrapped in triple single quotes)
    # =====================================================================
    new_layout_agent_code = '''class SelfHealingLayoutTokenAgent:
    def __init__(self, gateway: GatewaySimulator, model_name: str = "gemini-2.5-flash"):
        self.gateway = gateway
        self.agent = LlmAgent(
            name="Self_Healing_Layout_Token_Agent",
            model=model_name,
            description="Enforces design compliance on generated HTML copy, auto-correcting violations inline.",
            instruction="""
            You are the Self-Healing Layout Token Agent. Your job is to take an HTML block and fix any corporate design tokens or formatting violations.
            
            Corporate Design System Rules:
            1. Typography Scale: The main headline must be wrapped in <h1> and have style="font-size: 2.25rem; font-weight: 800; color: #FFFFFF;" (or equivalent class).
            2. Legal Footer: There must be a footer section at the very bottom wrapped in <div class="legal-footer"> or <div style="margin-top: 40px; border-top: 1px solid #374151; padding-top: 16px;">.
            3. Disclaimer Text: The footer must contain the text: "Disclosure: Product-A (compound_alpha) safety profile is based on Regulatory Compliance Vault Ref #V-2026-KTS99. Subject to local regulatory guidelines."
            4. Layout Overlap Prevention: The footer must have a style of "margin-top: auto;" or "margin-top: 40px;" to ensure clear visual separation from copy.
            
            Review the provided HTML. If any of these rules are violated, REWRITE the HTML to fix the violations. Do NOT change the core medical copy or claims. Return ONLY the complete, corrected HTML code block, with no additional conversational text.
            """
        )

    async def validate_and_heal_layout(self, html_content: str, log_callback, medication: str = "Product-A", safety_ref: str = "Ref #V-2026-KTS99") -> Tuple[bool, str, List[str]]:
        await log_callback("Self_Healing_Layout_Token_Agent", "Evaluating HTML layout against corporate style token registry...")
        await asyncio.sleep(0.4)
        
        violations = []
        is_compliant = True
        
        # Programmatic checks
        if "h1" not in html_content.lower() and "font-size: 2.25rem" not in html_content.lower():
            is_compliant = False
            violations.append("Violation: Main headline does not use H1 typographic scale (2.25rem).")
            await log_callback("Self_Healing_Layout_Token_Agent", "❌ LAYOUT VIOLATION: Typographic scale out of bounds (No H1 scale found).")

        if "legal-footer" not in html_content.lower() and "margin-top:" not in html_content.lower():
            is_compliant = False
            violations.append("Violation: Legal footer section is missing or lacks proper margins, risking overlap.")
            await log_callback("Self_Healing_Layout_Token_Agent", "❌ LAYOUT VIOLATION: Missing legal footer separation margin (risks layout overlap).")

        if "disclosure:" not in html_content.lower() and "compliance_vault" not in html_content.lower():
            is_compliant = False
            violations.append("Violation: Mandatory regulatory disclosure text is missing or out of sync.")
            await log_callback("Self_Healing_Layout_Token_Agent", "❌ LAYOUT VIOLATION: Missing mandatory FDA/Regulatory Compliance Vault regulatory disclosures.")

        if not is_compliant:
            await log_callback("Self_Healing_Layout_Token_Agent", "🔧 SELF-HEALING: Initiating LLM-powered inline layout restoration...")
            
            try:
                # Execute query with gateway resilience
                healed_html = await self.gateway.execute_with_resilience(
                    "Self_Healing_Layout_Token_Agent",
                    self.agent,
                    html_content
                )
                
                if "```html" in healed_html:
                    healed_html = healed_html.split("```html")[1].split("```")[0].strip()
                elif "```" in healed_html:
                    healed_html = healed_html.split("```")[1].split("```")[0].strip()
                    
                await log_callback("Self_Healing_Layout_Token_Agent", "✨ SELF-HEALING COMPLETE: Corporate design tokens successfully re-injected. Layout boundaries restored.")
                return False, healed_html, violations
            except Exception as e:
                # Dynamic programmatic fallback repair
                await log_callback("Self_Healing_Layout_Token_Agent", f"⚠️ Self-healing API unavailable ({str(e)}). Deploying dynamic fallback layout repair...")
                healed_html = self.programmatic_repair(html_content, medication, safety_ref)
                return False, healed_html, violations
        
        await log_callback("Self_Healing_Layout_Token_Agent", "✅ LAYOUT COMPLIANCE: HTML layout matches all corporate style tokens and padding boundaries.")
        return True, html_content, []

    def programmatic_repair(self, html: str, medication: str = "Product-A", safety_ref: str = "Ref #V-2026-KTS99") -> str:
        """Dynamic programmatic fallback repair for layout boundary enforcement."""
        repaired = html
        if "h1" not in repaired.lower():
            repaired = f"<div class='canvas-card-rendered'><h1>{medication} Clinical Campaign</h1>{repaired}</div>"
            
        if "legal-footer" not in repaired.lower() and "disclosure:" not in repaired.lower():
            disclaimer = (
                f'<div class="legal-footer" style="margin-top: 40px; border-top: 1px solid #374151; padding-top: 16px; font-size: 0.75rem; color: #64748B;">'
                f'Disclosure: {medication} safety profile is based on Regulatory Compliance Vault {safety_ref}. '
                f'Subject to local regulatory guidelines.</div>'
            )
            repaired = repaired + "\\n" + disclaimer
            
        return repaired'''

    # =====================================================================
    # PROGRAMMATIC STR_REPLACE REFACTORING
    # =====================================================================
    
    # 1. Refactor SemanticClaimsGraphAgent
    # We locate class SemanticClaimsGraphAgent and replace everything up to the next class
    idx_claims = content.find("class SemanticClaimsGraphAgent:")
    idx_layout = content.find("class SelfHealingLayoutTokenAgent:")
    
    if idx_claims != -1 and idx_layout != -1:
        before = content[:idx_claims]
        after = content[idx_layout:]
        content = before + new_claims_agent_code + "\n\n\n" + after
        print("Programmatically refactored SemanticClaimsGraphAgent!")
    else:
        print("Error locating SemanticClaimsGraphAgent indices!")
        
    # 2. Refactor SelfHealingLayoutTokenAgent
    # We locate class SelfHealingLayoutTokenAgent and replace everything up to class MasterOrchestratorAgent
    idx_layout_new = content.find("class SelfHealingLayoutTokenAgent:")
    idx_orch = content.find("class MasterOrchestratorAgent:")
    
    if idx_layout_new != -1 and idx_orch != -1:
        before = content[:idx_layout_new]
        after = content[idx_orch:]
        content = before + new_layout_agent_code + "\n\n\n" + after
        print("Programmatically refactored SelfHealingLayoutTokenAgent!")
    else:
        print("Error locating SelfHealingLayoutTokenAgent indices!")

    # 3. Update MasterOrchestratorAgent __init__ to pass self.gateway
    content = content.replace(
        "self.claims_subagent = SemanticClaimsGraphAgent()", 
        "self.claims_subagent = SemanticClaimsGraphAgent(self.gateway)"
    )
    
    # 4. Update MasterOrchestratorAgent pipeline call to pass drug and safety ref dynamically
    old_pipeline_call = """claims_compliant, verified_html, claims_audit = await self.claims_subagent.validate_claims_in_html(draft_html, log_msg)
        
        # Step 4: Self-Healing Layout Token Verification
        layout_compliant, final_html, layout_violations = await self.layout_subagent.validate_and_heal_layout(verified_html, log_msg)"""
    
    new_pipeline_call = """claims_compliant, verified_html, claims_audit = await self.claims_subagent.validate_claims_in_html(draft_html, log_msg)
        
        # Step 4: Self-Healing Layout Token Verification
        med = brief_data.get("Medication", "Product-A")
        safety_ref = self.claims_subagent.material_review_db.get("product_a_safety", {}).get("source_ref", "Ref #V-2026-KTS99")
        layout_compliant, final_html, layout_violations = await self.layout_subagent.validate_and_heal_layout(verified_html, log_msg, med, safety_ref)"""
        
    content = content.replace(old_pipeline_call, new_pipeline_call)
    
    with open(agents_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Core Backend Agents Refactored Programmatically & Successfully!")

if __name__ == "__main__":
    refactor_agents()
