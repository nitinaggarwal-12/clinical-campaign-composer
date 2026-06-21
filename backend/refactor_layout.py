import os

def refactor_layout():
    html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend", "index.html")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # =====================================================================
    # 1. NEW UNIFIED CLINICAL INGESTION HUB CARD (Dropzone + URL Fetcher)
    # =====================================================================
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

    # =====================================================================
    # 2. RESTRUCTURED CLINICAL DATASET REPOSITORY CARD (JSON List Only)
    # =====================================================================
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

    # =====================================================================
    # 3. CLEAN LIVE MARKETING CANVAS CARD (Pure Output + Clean Placeholder)
    # =====================================================================
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

    # =====================================================================
    # SLICING AND REPLACING INDEX.HTML SCTIONS
    # =====================================================================
    
    # 1. Locate the middle row grid container:
    # <div style="display: grid; grid-template-columns: 1.2fr 1.8fr; gap: 1.25rem; margin-top: 1.25rem;">
    # It contains Oncology Webhook Card and the old Clinical Repository Card.
    # We will replace it with a clean layout:
    # Oncology Webhook Card (Left) and a new grid holding (Ingestion Hub & Clinical Repository) (Right)
    
    # Let's locate the entire middle row block:
    start_grid = content.find('<!-- Middle Row: Webhook & Ingestion Repo -->')
    end_grid = content.find('<!-- Section C: Chat Rail communicating with Master Orchestrator -->')
    
    if start_grid != -1 and end_grid != -1:
        # Build the restructured middle row!
        restructured_middle_row = """<!-- Middle Row: Unified Ingestion, Webhook & Repository -->
                        <div style="display: grid; grid-template-columns: 1.1fr 1.9fr; gap: 1.25rem; margin-top: 1.25rem;">
                            <!-- Oncology Webhook card (Compact Left Column) -->
                            <div class="workspace-panel webhook-card" style="padding: 1.25rem 1.5rem; display: flex; flex-direction: column; justify-content: space-between; border-left: 4px solid var(--color-secondary); gap: 0.75rem;">
                                <div class="panel-header-compact">
                                    <span class="panel-icon">🌐</span>
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
        print("Error: Could not locate Ingestion grid section indices!")

    # 2. Locate and replace the Canvas Container on the right column
    start_canvas = content.find('<div class="canvas-container flex-col"')
    # Find the closing panel-header and panel-body
    end_canvas = content.find('</section>', start_canvas)
    
    # We want to replace the canvas-container inside the canvas-panel
    if start_canvas != -1 and end_canvas != -1:
        before = content[:start_canvas]
        after = content[end_canvas:]
        content = before + new_canvas_container + "\n                    " + after
        print("Restructured Canvas Container successfully!")
    else:
        print("Error: Could not locate Canvas container indices!")
        
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("HTML Workflow Layout Refactored Perfectly!")

if __name__ == "__main__":
    refactor_layout()
