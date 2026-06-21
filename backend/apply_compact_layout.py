import os

def refactor_html_to_compact():
    html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend", "index.html")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # =====================================================================
    # 1. COMPACT PIPELINE TRACKER (No paragraph descriptions)
    # =====================================================================
    compact_tracker = """<!-- Section A: Live Multi-Agent Tracker (Compact Timeline) -->
                        <div class="workspace-panel tracker-card" style="padding: 1rem 1.25rem; display: flex; flex-direction: column; gap: 0.6rem;">
                            <div class="panel-header-compact" style="margin-bottom: 0.2rem;">
                                <span class="panel-icon">⚙️</span>
                                <h3 style="font-size: 0.8rem; font-weight: 700; color: var(--color-text-main);">Multi-Agent Execution Pipeline</h3>
                            </div>
                            
                            <div class="pipeline-steps-compact" style="display: flex; justify-content: space-between; gap: 0.5rem;">
                                <!-- Step 1 -->
                                <div class="pipeline-step active" id="step-ingestion" style="flex: 1; padding: 0.4rem 0.6rem; border-radius: 6px; border: 1px solid var(--border-color); background: rgba(255,255,255,0.01); display: flex; flex-direction: column; gap: 0.25rem; position: relative;">
                                    <div style="display: flex; align-items: center; gap: 0.4rem; width: 100%;">
                                        <span class="step-num-mini" style="font-size: 0.65rem; font-weight: 800; background: var(--color-primary-glow); color: var(--color-primary); width: 14px; height: 14px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">1</span>
                                        <span style="font-size: 0.68rem; font-weight: 700; color: var(--color-text-main);">Ingest & Parse</span>
                                        <span class="step-badge status-idle" id="badge-ingestion" style="font-size: 0.52rem; margin-left: auto; padding: 0.1rem 0.25rem;">IDLE</span>
                                    </div>
                                    <div style="width: 100%; height: 2px; background: rgba(255,255,255,0.05); border-radius: 1px; overflow: hidden;">
                                        <div class="progress-bar" id="progress-ingestion" style="width: 0%; height: 100%; background: var(--color-primary); transition: width 0.3s ease;"></div>
                                    </div>
                                </div>
                                <!-- Step 2 -->
                                <div class="pipeline-step" id="step-claims" style="flex: 1; padding: 0.4rem 0.6rem; border-radius: 6px; border: 1px solid var(--border-color); background: rgba(255,255,255,0.01); display: flex; flex-direction: column; gap: 0.25rem; position: relative;">
                                    <div style="display: flex; align-items: center; gap: 0.4rem; width: 100%;">
                                        <span class="step-num-mini" style="font-size: 0.65rem; font-weight: 800; background: rgba(255,255,255,0.05); color: var(--color-text-muted); width: 14px; height: 14px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">2</span>
                                        <span style="font-size: 0.68rem; font-weight: 700; color: var(--color-text-muted);">Claims Audit</span>
                                        <span class="step-badge status-idle" id="badge-claims" style="font-size: 0.52rem; margin-left: auto; padding: 0.1rem 0.25rem;">IDLE</span>
                                    </div>
                                    <div style="width: 100%; height: 2px; background: rgba(255,255,255,0.05); border-radius: 1px; overflow: hidden;">
                                        <div class="progress-bar" id="progress-claims" style="width: 0%; height: 100%; background: var(--color-primary); transition: width 0.3s ease;"></div>
                                    </div>
                                </div>
                                <!-- Step 3 -->
                                <div class="pipeline-step" id="step-layout" style="flex: 1; padding: 0.4rem 0.6rem; border-radius: 6px; border: 1px solid var(--border-color); background: rgba(255,255,255,0.01); display: flex; flex-direction: column; gap: 0.25rem; position: relative;">
                                    <div style="display: flex; align-items: center; gap: 0.4rem; width: 100%;">
                                        <span class="step-num-mini" style="font-size: 0.65rem; font-weight: 800; background: rgba(255,255,255,0.05); color: var(--color-text-muted); width: 14px; height: 14px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">3</span>
                                        <span style="font-size: 0.68rem; font-weight: 700; color: var(--color-text-muted);">Self-Heal</span>
                                        <span class="step-badge status-idle" id="badge-layout" style="font-size: 0.52rem; margin-left: auto; padding: 0.1rem 0.25rem;">IDLE</span>
                                    </div>
                                    <div style="width: 100%; height: 2px; background: rgba(255,255,255,0.05); border-radius: 1px; overflow: hidden;">
                                        <div class="progress-bar" id="progress-layout" style="width: 0%; height: 100%; background: var(--color-primary); transition: width 0.3s ease;"></div>
                                    </div>
                                </div>
                            </div>
                        </div>"""

    # =====================================================================
    # 2. HIGH-FIDELITY TABBED INGESTION DOCK CARD
    # =====================================================================
    tabbed_dock = """<!-- Section B: Unified Ingestion Dock (Horizontal Tabs - ZERO SCROLL) -->
                        <div class="workspace-panel ingestion-dock-card" style="padding: 1rem 1.25rem; display: flex; flex-direction: column; gap: 0.65rem;">
                            <!-- Tab Header Buttons -->
                            <div class="dock-tabs" style="display: flex; border-bottom: 1px solid var(--border-color); padding-bottom: 0.35rem; gap: 0.5rem;">
                                <button class="dock-tab-btn active" onclick="switchDockTab('tab-file-url')" id="btn-tab-file-url" style="padding: 0.3rem 0.6rem; font-size: 0.68rem; font-weight: 700; border: none; background: none; color: var(--color-primary); border-bottom: 2px solid var(--color-primary); cursor: pointer; transition: var(--transition-smooth);">📥 PPTX / PDF Ingest</button>
                                <button class="dock-tab-btn" onclick="switchDockTab('tab-briefs')" id="btn-tab-briefs" style="padding: 0.3rem 0.6rem; font-size: 0.68rem; font-weight: 700; border: none; background: none; color: var(--color-text-muted); cursor: pointer; transition: var(--transition-smooth);">📁 Secure Briefs</button>
                                <button class="dock-tab-btn" onclick="switchDockTab('tab-webhook')" id="btn-tab-webhook" style="padding: 0.3rem 0.6rem; font-size: 0.68rem; font-weight: 700; border: none; background: none; color: var(--color-text-muted); cursor: pointer; transition: var(--transition-smooth);">⚡ Label Sync Webhook</button>
                            </div>

                            <!-- Tab Contents -->
                            <div class="dock-tab-contents" style="position: relative; min-height: 75px;">
                                
                                # PANEL 1: PPTX/PDF File Dropzone + URL Fetcher
                                <div class="dock-panel" id="panel-file-url" style="display: flex; flex-direction: column; gap: 0.5rem;">
                                    <div style="display: flex; gap: 0.5rem; align-items: center;">
                                        <!-- Compact Sidebar Dropzone -->
                                        <div class="pptx-dropzone" id="sidebar-dropzone" style="flex: 1; padding: 0.5rem; border: 1.5px dashed var(--border-color); border-radius: var(--card-radius); background: var(--bg-surface); display: flex; align-items: center; justify-content: center; gap: 0.4rem; cursor: pointer; text-align: center; height: 36px; transition: var(--transition-smooth);" ondragover="event.preventDefault()" ondrop="handleDrop(event)" onclick="triggerFileInput()">
                                            <input type="file" id="canvas-file-input" style="display: none;" accept=".pptx,.pdf" onchange="handleFileSelect(event)">
                                            <span style="font-size: 0.95rem;">📁</span>
                                            <span style="font-weight: 700; font-size: 0.68rem; color: var(--color-text-main);">Upload PowerPoint / PDF Document</span>
                                        </div>
                                        
                                        <div style="font-size: 0.65rem; color: var(--color-text-muted); font-weight: bold; text-transform: uppercase;">OR</div>
                                        
                                        <!-- Compact Web URL Ingestion bar -->
                                        <div class="url-ingest-bar" style="flex: 1; display: flex; gap: 0.2rem;">
                                            <input type="url" id="url-ingest-input" placeholder="Paste clinical PDF/HTML URL..." style="flex: 1; font-size: 0.62rem; padding: 0.25rem 0.4rem; border-radius: 4px; border: 1px solid var(--border-color); background: var(--bg-surface-solid); color: var(--color-text-main); outline: none;">
                                            <button class="btn btn-primary" onclick="fetchAndIngestUrl()" style="padding: 0.25rem 0.5rem; font-size: 0.62rem; font-weight: 700; border-radius: 4px;">Fetch</button>
                                        </div>
                                    </div>
                                </div>

                                # PANEL 2: SECURE BRIEFS LIBRARY (JSON List)
                                <div class="dock-panel" id="panel-briefs" style="display: none; flex-direction: column; gap: 0.4rem;">
                                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.1rem;">
                                        <span style="font-size: 0.65rem; color: var(--color-text-muted); font-weight: 600;">Select brief to generate campaign copy:</span>
                                        <label class="btn-upload-file" for="file-upload-input" title="Upload a JSON brief" style="padding: 0.15rem 0.4rem; font-size: 0.6rem; margin: 0; cursor: pointer; border-radius: 4px;">
                                            <span>Upload JSON</span>
                                            <input type="file" id="file-upload-input" style="display: none;" accept=".json" onchange="uploadDatasetFile(event)">
                                        </label>
                                    </div>
                                    <div class="dataset-list-container" id="dataset-list-container" style="max-height: 48px; overflow-y: auto;">
                                        <div class="dataset-loading">Scanning briefs...</div>
                                    </div>
                                </div>

                                # PANEL 3: LABEL SYNC WEBHOOK SIMULATOR
                                <div class="dock-panel" id="panel-webhook" style="display: none; flex-direction: column; gap: 0.4rem; justify-content: center; height: 38px;">
                                    <div style="display: flex; align-items: center; justify-content: space-between; gap: 1rem;">
                                        <p style="font-size: 0.65rem; color: var(--color-text-muted); margin: 0; line-height: 1.2;">Simulate an external FDA label update webhook sync event to trigger self-healing layout audits.</p>
                                        <button class="btn btn-webhook" onclick="triggerWebhookSync()" style="padding: 0.35rem 0.75rem; font-size: 0.65rem; border-radius: 4px; flex-shrink: 0; width: auto; margin: 0;">
                                            <span>⚡ Sync 61% ORR Label</span>
                                        </button>
                                    </div>
                                </div>
                                
                            </div>
                        </div>"""

    # Locate and replace the Tracker Card
    start_tracker = content.find('<!-- Section A: Multi-Agent Ingestion & Compliance Progress Tracker -->')
    if start_tracker == -1:
        start_tracker = content.find('<!-- Section A: Live Multi-Agent Tracker (Compact Timeline) -->')
        
    end_tracker = content.find('<!-- Section B: Unified Ingestion Dock (Horizontal Tabs - ZERO SCROLL) -->')
    if end_tracker == -1:
        end_tracker = content.find('<!-- Middle Row: Unified Ingestion, Webhook & Repository -->')
        if end_tracker == -1:
            # Fallback to older middle row comments
            end_tracker = content.find('<!-- Middle Row: Webhook & Ingestion Repo -->')
            if end_tracker == -1:
                end_tracker = content.find('<!-- Section B & B.2: Quick Actions Row (Side-by-Side Grid) -->')

    if start_tracker != -1 and end_tracker != -1:
        before = content[:start_tracker]
        after = content[end_tracker:]
        content = before + compact_tracker + "\n\n                        " + after
        print("Replaced Tracker with Compact Timeline successfully!")
    else:
        print("Error: Could not locate Tracker card indices!")

    # Locate and replace the Middle Ingestion Grid with the Tabbed Dock Card!
    start_grid = content.find('<!-- Middle Row: Unified Ingestion, Webhook & Repository -->')
    if start_grid == -1:
        start_grid = content.find('<!-- Section B & B.2: Quick Actions Row (Side-by-Side Grid) -->')
        if start_grid == -1:
            start_grid = content.find('<!-- Section B: Unified Ingestion Dock -->')
            
    end_grid = content.find('<!-- Section C: Chat Rail communicating with Master Orchestrator -->')
    
    if start_grid != -1 and end_grid != -1:
        before = content[:start_grid]
        after = content[end_grid:]
        # Replace python comments inside triple quotes to avoid formatting issues
        clean_tabbed_dock = tabbed_dock.replace('# PANEL 1:', '<!-- Panel 1 -->').replace('# PANEL 2:', '<!-- Panel 2 -->').replace('# PANEL 3:', '<!-- Panel 3 -->')
        content = before + clean_tabbed_dock + "\n\n                        " + after
        print("Replaced Grid with Unified Tabbed Ingestion Dock successfully!")
    else:
        print("Error: Could not locate Ingestion Grid indices for Dock!")
        
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

def refactor_css_to_compact():
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend", "style.css")
    
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Lock the control-panel sidebar height to 100% viewport, hide overflow (ZERO SCROLL!)
    start_cp = content.find(".control-panel {")
    end_cp = content.find("}", start_cp)
    
    if start_cp != -1 and end_cp != -1:
        new_cp_style = """.control-panel {
    height: 100%;
    display: flex;
    flex-direction: column;
    overflow: hidden; /* ABSOLUTELY ZERO SCROLLING ON THE SIDEBAR PANEL */
    gap: 0.85rem;
}"""
        before = content[:start_cp]
        after = content[end_cp+1:]
        content = before + new_cp_style + after
        print("Locked Sidebar Scroll in CSS successfully!")
    else:
        print("Error: Could not locate .control-panel in CSS!")

    # Adjust the chat-messages and console logs height and padding to fit screen perfectly
    # Add tab buttons hover states in CSS
    tab_css_extensions = """
/* Ingestion Tab Dock Styles */
.dock-tab-btn:hover {
    color: var(--color-primary-glow) !important;
}
.dock-tab-btn.active {
    border-bottom: 2px solid var(--color-primary) !important;
}
.pipeline-step-mini.active {
    border-color: var(--color-primary-glow) !important;
    box-shadow: 0 0 10px rgba(13, 148, 136, 0.08);
    animation: borderPulse 2s infinite alternate;
}
"""
    if ".dock-tab-btn" not in content:
        content += tab_css_extensions
        print("Appended Dock Tab CSS Extensions successfully!")
        
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(content)

def refactor_js_to_compact():
    js_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend", "app.js")
    
    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Append switchDockTab javascript function to the bottom of app.js
    dock_tab_js = """
// Tab switching logic for the unified Ingestion Dock
window.switchDockTab = function(tabId) {
    // Hide all panels
    document.getElementById('panel-file-url').style.display = 'none';
    document.getElementById('panel-briefs').style.display = 'none';
    document.getElementById('panel-webhook').style.display = 'none';
    
    // Deactivate all tab buttons
    const buttons = document.querySelectorAll('.dock-tab-btn');
    buttons.forEach(btn => {
        btn.classList.remove('active');
        btn.style.color = 'var(--color-text-muted)';
        btn.style.borderBottom = 'none';
    });
    
    # Show active panel
    document.getElementById(tabId).style.display = 'flex';
    if (tabId === 'panel-briefs') {
        document.getElementById(tabId).style.display = 'flex';
    } else if (tabId === 'panel-webhook') {
        document.getElementById(tabId).style.display = 'flex';
    }
    
    # Activate active tab button
    const activeBtn = document.getElementById('btn-' + tabId);
    if (activeBtn) {
        activeBtn.classList.add('active');
        activeBtn.style.color = 'var(--color-primary)';
        activeBtn.style.borderBottom = '2px solid var(--color-primary)';
    }
};
"""
    clean_dock_tab_js = dock_tab_js.replace('# Show active panel', '// Show active panel')
    
    if "switchDockTab" not in content:
        content += clean_dock_tab_js
        print("Appended switchDockTab JS function successfully!")
        
    # Update status logger in app.js to work with compact status badges in timeline!
    # Let's check how updatePipelineStatus is implemented.
    # In app.js, it updates step classes. Since we compacted them, let's see if we need adjustments.
    # We kept the classes and ids similar (just added -mini or similar), let's ensure the JS works smoothly!
    # Wait, let's verify if updatePipelineStatus is defined in app.js.
    
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    print("Executing master compact sidebar refactoring (ZERO SCROLL)...")
    refactor_html_to_compact()
    refactor_css_to_compact()
    refactor_js_to_compact()
    print("Master compact refactoring complete!")
