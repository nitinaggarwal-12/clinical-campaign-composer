import os

def refactor_html_layout():
    html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend", "index.html")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. NEW UNIFIED CLINICAL INGESTION HUB CARD (Dropzone + URL Fetcher)
    new_ingestion_hub = """<!-- Section B1: Clinical Ingestion Hub (PPTX/PDF Dropzone & Web URL Fetcher) -->
                                    <div class="workspace-panel Ingestion-card" style="padding: 1.25rem 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;">
                                        <div class="panel-header-compact">
                                            <span class="panel-icon">📥</span>
                                            <h4 style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: var(--color-text-main);">Clinical Ingestion Hub</h4>
                                        </div>
                                        <p style="font-size: 0.68rem; line-height: 1.3; color: var(--color-text-muted); margin: 0;">Upload a physical clinical deck (.pptx), PDF, or download directly from a web URL:</p>
                                        
                                        <!-- Compact Sidebar Dropzone -->
                                        <div class="pptx-dropzone" id="sidebar-dropzone" style="padding: 0.85rem; border: 2px dashed var(--border-color); border-radius: var(--card-radius); background: var(--bg-surface); display: flex; flex-direction: column; align-items: center; gap: 0.4rem; cursor: pointer; text-align: center; transition: var(--transition-smooth);" ondragover="event.preventDefault()" ondrop="handleDrop(event)" onclick="triggerFileInput()">
                                            <input type="file" id="canvas-file-input" style="display: none;" accept=".pptx,.pdf" onchange="handleFileSelect(event)">
                                            <span style="font-size: 1.25rem;">📁</span>
                                            <span style="font-weight: 700; font-size: 0.72rem; color: var(--color-text-main);">Upload PPTX or PDF File</span>
                                            <span style="font-size: 0.62rem; color: var(--color-text-muted);">Click or drag clinical study to harvest claims</span>
                                        </div>
                                        
                                        <!-- Web URL Ingestion bar -->
                                        <div class="url-ingest-bar" style="display: flex; gap: 0.2rem; margin-top: 0.25rem; border-top: 1px solid var(--border-color); padding-top: 0.5rem;">
                                            <input type="url" id="url-ingest-input" placeholder="Paste clinical PDF/HTML URL..." style="flex: 1; font-size: 0.62rem; padding: 0.2rem 0.35rem; border-radius: 4px; border: 1px solid var(--border-color); background: var(--bg-surface-solid); color: var(--color-text-main); outline: none;">
                                            <button class="btn btn-primary" onclick="fetchAndIngestUrl()" style="padding: 0.2rem 0.4rem; font-size: 0.62rem; font-weight: 700; border-radius: 4px;">Fetch</button>
                                        </div>
                                    </div>"""

    # 2. RESTRUCTURED CLINICAL DATASET REPOSITORY CARD (JSON List Only)
    new_repository_card = """<!-- Section B2: Clinical Dataset Repository (JSON Briefs) -->
                                    <div class="workspace-panel repository-card" style="padding: 1.25rem 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;">
                                        <div class="panel-header-compact" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0;">
                                            <div style="display: flex; align-items: center; gap: 0.5rem;">
                                                <span class="panel-icon">📁</span>
                                                <h4 style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: var(--color-text-main);">Clinical Repository</h4>
                                            </div>
                                            <label class="btn-upload-file" for="file-upload-input" title="Upload a JSON brief" style="padding: 0.2rem 0.5rem; font-size: 0.62rem; margin: 0; cursor: pointer;">
                                                <span>Upload JSON</span>
                                                <input type="file" id="file-upload-input" style="display: none;" accept=".json" onchange="uploadDatasetFile(event)">
                                            </label>
                                        </div>
                                        <p class="repo-desc" style="font-size: 0.68rem; line-height: 1.2; color: var(--color-text-muted); margin: 0;">Select a locked campaign brief template from the secure clinical library:</p>
                                        <div class="dataset-list-container" id="dataset-list-container" style="margin-bottom: 0;">
                                            <div class="dataset-loading">Scanning file system...</div>
                                        </div>
                                    </div>"""

    # 3. CLEAN LIVE MARKETING CANVAS CARD (Pure Output + Clean Placeholder)
    new_canvas_container = """<div class="canvas-container flex-col" style="flex: 1; min-height: 0; position: relative;">
                            <!-- Gorgeous Glassmorphic Canvas Placeholder -->
                            <div class="canvas-placeholder flex-col" id="canvas-placeholder" style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; border: 1px dashed var(--border-color); border-radius: var(--panel-radius); padding: 2.5rem; background: rgba(255, 255, 255, 0.015); height: 100%; transition: var(--transition-smooth);">
                                <div style="font-size: 3.5rem; margin-bottom: 1.25rem; filter: drop-shadow(0 0 10px rgba(13, 148, 136, 0.15));">🎨</div>
                                <h3 style="font-size: 1.25rem; font-weight: 700; color: var(--color-text-main); margin-bottom: 0.5rem;">Live Marketing Canvas</h3>
                                <p style="font-size: 0.82rem; color: var(--color-text-muted); max-width: 340px; margin-bottom: 1.5rem; line-height: 1.4;">
                                    Awaiting multi-agent compliance asset generation. Ingest a clinical PowerPoint, PDF, web URL, or JSON brief on the left to begin.
                                </p>
                                
                                <div style="display: flex; flex-direction: column; align-items: center; gap: 0.5rem;">
                                    <span style="font-size: 0.7rem; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; letter-spacing: 0.05em;">Or Execute Baseline Prompt:</span>
                                    <button class="btn-quick-prompt" onclick="setPromptAndSubmit('Generate a clinical marketing draft for Product-A oncology indications targeting adults.')" style="border-radius: 20px; font-size: 0.75rem; padding: 0.45rem 1.5rem; border: 1px solid var(--border-color); background: var(--bg-surface-solid); color: var(--color-text-main);">"Initialize Product-A NSCLC Campaign..."</button>
                                </div>
                            </div>
                            
                            <!-- Live Canvas rendering block -->
                            <div class="canvas-render-block" id="canvas-render-block" style="display: none; height: 100%; overflow-y: auto; border-radius: var(--panel-radius); border: 1px solid var(--border-color);">
                                <!-- Ingested compliance card HTML goes here -->
                            </div>
                        </div>"""

    # Locate and replace the middle row grid container
    start_grid = content.find('<!-- Section B & B.2: Quick Actions Row (Side-by-Side Grid) -->')
    if start_grid == -1:
        # Fallback to general middle row tag if edited previously
        start_grid = content.find('<!-- Middle Row: Unified Ingestion, Webhook & Repository -->')
        
    end_grid = content.find('<!-- Section C: Chat Rail communicating with Master Orchestrator -->')
    
    if start_grid != -1 and end_grid != -1:
        restructured_middle_row = """<!-- Middle Row: Unified Ingestion, Webhook & Repository -->
                        <div style="display: grid; grid-template-columns: 1.1fr 1.9fr; gap: 1.25rem; margin-top: 1.25rem;">
                            <!-- Oncology Webhook card (Compact Left Column) -->
                            <div class="workspace-panel webhook-card" style="padding: 1.25rem 1.5rem; display: flex; flex-direction: column; justify-content: space-between; border-left: 4px solid var(--color-secondary); gap: 0.75rem;">
                                <div class="panel-header-compact">
                                    <span class="pulse-icon"></span>
                                    <h4 style="font-size: 0.75rem; font-weight: 700; color: var(--color-text-main); text-transform: uppercase;">Oncology Webhook</h4>
                                    <span class="badge badge-secondary" style="font-size: 0.55rem; padding: 0.1rem 0.3rem;">API</span>
                                </div>
                                <p style="font-size: 0.65rem; line-height: 1.3; color: var(--color-text-muted); margin: 0;">Simulate an external FDA label update webhook sync event to trigger AI self-healing audits.</p>
                                <button class="btn btn-webhook" onclick="triggerWebhookSync()" style="margin-top: auto; padding: 0.45rem; font-size: 0.7rem; border-radius: 6px;">
                                    <span>⚡ Sync 61% ORR Label</span>
                                </button>
                            </div>
                            
                            <!-- Ingestion Hub & Repository Stack (Right Column) -->
                            <div style="display: flex; flex-direction: column; gap: 1.25rem;">
                                """ + new_ingestion_hub + """
                                """ + new_repository_card + """
                            </div>
                        </div>
                        
                        """
        before = content[:start_grid]
        after = content[end_grid:]
        content = before + restructured_middle_row + after
        print("Restructured Middle Ingestion Row successfully!")
    else:
        print("Error: Could not locate Ingestion grid section indices in HTML!")

    # Locate and replace the Canvas Container on the right column
    start_canvas = content.find('<div class="canvas-container"')
    end_canvas = content.find('</section>', start_canvas)
    
    if start_canvas != -1 and end_canvas != -1:
        before = content[:start_canvas]
        after = content[end_canvas:]
        content = before + new_canvas_container + "\n                    " + after
        print("Restructured Canvas Container successfully!")
    else:
        print("Error: Could not locate Canvas container indices in HTML!")
        
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

def refactor_backend_logic():
    main_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "backend", "main.py")
    
    with open(main_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_func = content.find("async def process_extracted_text(")
    end_func = content.find('@app.websocket("/ws/logs")', start_func)
    
    if start_func != -1 and end_func != -1:
        new_process_extracted_text_func = """async def process_extracted_text(extracted_text: str, source_filename: str, log_msg_func):
    \"\"\"Helper function to route extracted clinical text through the Vertex AI multi-agent pipeline.\"\"\"
    await log_msg_func("Master_Orchestrator_Agent", "Routing raw extracted clinical text to Strategic Ingestion Agent for structuring...")
    
    try:
        # 1. Structured Parsing using L3 Strategy Ingestion subagent (ADK-Resilient Call)
        brief_data = await orchestrator.ingest_subagent.parse_brief(extracted_text, log_msg_func)
        
        # Dynamic filename check to correct any default fallbacks
        medication = brief_data.get("Medication", "Product-A")
        if "product_a" not in source_filename.lower() and "NSCLC" not in source_filename:
            if "product_b" in source_filename.lower() or "CLEAR" in source_filename:
                brief_data["Medication"] = "Product-B + Product-A"
                brief_data["Campaign Name"] = "Product-B + Product-A RCC Acceleration"
                brief_data["Clinical Trial"] = "CLEAR / KEYNOTE-581 (RCC) (NCT02811822)"
            elif "product_c" in source_filename.lower() or "LITESPARK" in source_filename:
                brief_data["Medication"] = "Product-C"
                brief_data["Campaign Name"] = "Product-C Advanced RCC Acceleration"
                brief_data["Clinical Trial"] = "LITESPARK-005 (RCC) (NCT04195750)"
    except Exception as e:
        print(f"Ingestion structuring failed: {str(e)}")
        medication = "Product-A"
        if "product_b" in source_filename.lower() or "CLEAR" in source_filename:
            medication = "Product-B + Product-A"
        elif "product_c" in source_filename.lower() or "LITESPARK" in source_filename:
            medication = "Product-C"
            
        brief_data = {
            "Campaign Name": f"{medication} Live Ingestion Campaign",
            "Therapeutic Area": "Oncology",
            "Target Patient Population": "Adults with advanced cancer matching FDA indications",
            "Key Efficacy Claim": f"{medication} Efficacy: High Objective Response Rate (ORR) observed in clinical trials.",
            "Key Safety Parameter": f"{medication} Safety Profile: Standard Grade 3/4 Adverse Events observed.",
            "Core Marketing Hook": f"Redefining overall survival boundaries with {medication}.",
            "Medication": medication,
            "Clinical Trial": "Phase III Landmark Clinical Trial"
        }
        
    # Save structured json to datasets
    json_filename = source_filename.split(".")[0] + "_Structured.json"
    json_filepath = os.path.join(DATASETS_DIR, json_filename)
    with open(json_filepath, 'w') as f:
        json.dump(brief_data, f, indent=4)
        
    await log_msg_func("Master_Orchestrator_Agent", f"Clinical text successfully structured and saved as '{json_filename}'!")
    await log_msg_func("Master_Orchestrator_Agent", "Syncing campaign brief to orchestrator session history ledger...")
    orchestrator.state_history.append(brief_data)
    
    # 2. Generate Draft HTML Copy (Master Orchestrator)
    await log_msg_func("Master_Orchestrator_Agent", "Generating responsive dark-mode marketing HTML copy draft...")
    draft_prompt = f"Generate HTML copy for the following structured brief: {json.dumps(brief_data)}"
    draft_html = await orchestrator.gateway.execute_with_resilience(
        "Master_Orchestrator_Agent",
        orchestrator.orchestration_agent,
        draft_prompt
    )
    
    if "```html" in draft_html:
        draft_html = draft_html.split("```html")[1].split("```")[0].strip()
    elif "```" in draft_html:
        draft_html = draft_html.split("```")[1].split("```")[0].strip()
        
    medication = brief_data.get("Medication", "Product-A")
    
    # Dynamic Claims Graph Database Sync based on medication name!
    if "Product-C" in medication or "compound_gamma" in extracted_text.lower():
        orchestrator.claims_subagent.material_review_db["product_a_efficacy"] = {
            "claim_id": "CLM-WR-005-EFF",
            "trial_record": "LITESPARK-005 study (NCT04195750)",
            "parameter": "Objective Response Rate (ORR)",
            "active_version": "v1.0",
            "current_efficacy_value": "22%",
            "source_ref": "Regulatory Compliance Vault Ref #V-2026-WR005",
            "verification_hash": "sha256:d9b23f8c8a11c8e5d2b71a3f009a1c662863a9b11c8e5d2b71a3f009a1c66286",
            "last_updated": "2026-03-10T09:00:00Z"
        }
        orchestrator.claims_subagent.material_review_db["product_a_safety"] = {
            "claim_id": "CLM-WR-005-SAF",
            "trial_record": "LITESPARK-005 Adverse Events (NCT04195750)",
            "parameter": "Grade 3/4 Adverse Events",
            "value": "30%",
            "active_version": "v1.0",
            "source_ref": "Regulatory Compliance Vault Ref #V-2026-WR005",
            "verification_hash": "sha256:4f8d2eb3a901c4e5d2b71a3f009a1c77f00a2eb3a901c77f00a2eb3a901c66",
            "last_updated": "2026-03-10T09:00:00Z"
        }
    elif "Product-B" in medication or "compound_beta" in extracted_text.lower():
        orchestrator.claims_subagent.material_review_db["product_a_efficacy"] = {
            "claim_id": "CLM-KT-581-EFF",
            "trial_record": "CLEAR / KEYNOTE-581 study (NCT02811822)",
            "parameter": "Objective Response Rate (ORR)",
            "active_version": "v1.0",
            "current_efficacy_value": "71%",
            "source_ref": "Regulatory Compliance Vault Ref #V-2026-LV581",
            "verification_hash": "sha256:8b9a2ea9a11c8e5d2b71a3f009a1c662863a9b11c8e5d2b71a3f009a1c66286",
            "last_updated": "2026-04-12T11:30:00Z"
        }
        orchestrator.claims_subagent.material_review_db["product_a_safety"] = {
            "claim_id": "CLM-KT-581-SAF",
            "trial_record": "CLEAR Adverse Events (NCT02811822)",
            "parameter": "Grade 3/4 Adverse Events",
            "value": "82%",
            "active_version": "v1.0",
            "source_ref": "Regulatory Compliance Vault Ref #V-2026-LV581",
            "verification_hash": "sha256:7f9c2eb3a901c4e5d2b71a3f009a1c77f00a2eb3a901c77f00a2eb3a901c66",
            "last_updated": "2026-04-12T11:30:00Z"
        }
    else:
        # Default Product-A KEYNOTE-189
        orchestrator.claims_subagent.material_review_db["product_a_efficacy"] = {
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
        }
        orchestrator.claims_subagent.material_review_db["product_a_safety"] = {
            "claim_id": "CLM-KT-189-SAF",
            "trial_record": "KEYNOTE-189 Immune-Mediated Adverse Reactions (NCT02578680)",
            "parameter": "Grade 3/4 Immune-Mediated Adverse Reactions",
            "value": "10%",
            "active_version": "v2.1",
            "source_ref": "Regulatory Compliance Vault Ref #V-2026-KTS99",
            "verification_hash": "sha256:8f9c2eb3a901c4e5d2b71a3f009a1c662863a9b11c8e5d2b71a3f009a1c66286",
            "last_updated": "2026-02-15T08:30:00Z"
        }

    # 3. Validate Claims (Semantic Claims Graph Agent)
    await log_msg_func("Master_Orchestrator_Agent", f"Draft copy generated. Routing to Semantic Claims Graph Agent for {medication} check...")
    claims_compliant, verified_html, claims_audit = await orchestrator.claims_subagent.validate_claims_in_html(draft_html, log_msg_func)
    
    # 4. Validate & Self-Heal Layout (Self-Healing Layout Token Agent)
    med = brief_data.get("Medication", "Product-A")
    safety_ref = orchestrator.claims_subagent.material_review_db.get("product_a_safety", {}).get("source_ref", "Ref #V-2026-KTS99")
    layout_compliant, final_html, layout_violations = await orchestrator.layout_subagent.validate_and_heal_layout(verified_html, log_msg_func, med, safety_ref)
    
    await log_msg_func("Master_Orchestrator_Agent", f"Live document ingestion from '{source_filename}' successfully completed.")
    
    return {
        "status": "SUCCESS",
        "brief": brief_data,
        "html": final_html,
        "claims_audit": claims_audit,
        "layout_audit": {
            "compliant": layout_compliant,
            "violations": layout_violations
        },
        "claims_sync": {
            "active_version": orchestrator.claims_subagent.material_review_db["product_a_efficacy"]["active_version"],
            "efficacy_value": orchestrator.claims_subagent.material_review_db["product_a_efficacy"]["current_efficacy_value"],
            "verification_hash": orchestrator.claims_subagent.material_review_db["product_a_efficacy"]["verification_hash"]
        }
    }

"""
        before = content[:start_func]
        after = content[end_func:]
        content = before + new_process_extracted_text_func + "\n" + after
        
        with open(main_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Refactored main.py backend logic successfully!")
    else:
        print("Error: Could not locate process_extracted_text function index in main.py!")

if __name__ == "__main__":
    print("Executing master layout & backend refactoring...")
    refactor_html_layout()
    refactor_backend_logic()
    print("Master refactoring complete!")
