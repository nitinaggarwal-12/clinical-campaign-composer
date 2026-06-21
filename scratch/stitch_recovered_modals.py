import re

html_path = "/Users/nitinagga/Documents/Maestro-Automated-Claims-Harvesting-&-Trigger-Pipeline/frontend/index.html"

print("Reading active index.html file...")
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Surgically rename the Vis.js network container in Phase 3
print("Renaming Vis.js network container to 'governance-ledger-network'...")
old_container = 'id="claims-network-container"'
new_container = 'id="governance-ledger-network"'

if old_container in content:
    content = content.replace(old_container, new_container)
    print("✅ Successfully renamed claims-network-container!")
else:
    print("⚠️ Warning: claims-network-container not found or already renamed.")

# 2. Define the 5 high-fidelity modals HTML string
modals_html = """
    <!-- =====================================================================
         GOOGLE MAESTRO COMPLIANCE & ORCHESTRATION SYSTEM MODALS
         ===================================================================== -->

    <!-- DETAIL MODAL FOR CLASSIFIED CLAIMS NODES -->
    <div class="imagen-modal-overlay" id="detail-modal">
        <div class="imagen-modal-card" style="max-width: 550px; width: 90%; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid var(--border-color); box-shadow: var(--shadow-xl);">
            <div class="imagen-modal-header" style="border-bottom: 1px solid var(--border-color); padding-bottom: 0.6rem; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 0.6rem;">
                    <span id="detail-modal-icon" style="font-size: 1.5rem;">🔍</span>
                    <div>
                        <h3 id="detail-modal-title" style="font-family: 'Outfit', sans-serif; font-weight: 800; margin: 0; color: var(--color-text-main);">Node Details</h3>
                        <p id="detail-modal-subtitle" style="font-size: 0.62rem; color: var(--color-text-muted); margin: 0.15rem 0 0 0;"></p>
                    </div>
                </div>
                <button class="imagen-modal-close" onclick="closeDetailModal()" style="background: none; border: none; color: var(--color-text-muted); font-size: 1.5rem; cursor: pointer; outline: none; transition: var(--transition-smooth);">&times;</button>
            </div>
            <div class="imagen-modal-body" style="padding-top: 1rem;">
                <div id="detail-modal-body" style="font-size: 0.72rem; line-height: 1.4; color: var(--color-text-main); max-height: 50vh; overflow-y: auto;">
                    <!-- Dynamic details go here -->
                </div>
            </div>
        </div>
    </div>

    <!-- FDA FORM 2253 TRANSMITTAL COMPILER MODAL -->
    <div class="imagen-modal-overlay" id="fda-2253-modal-overlay" style="display: none; justify-content: center; align-items: center; z-index: 10000; background: rgba(0, 0, 0, 0.6); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);">
        <div class="imagen-modal-card" style="max-width: 850px; width: 95%; max-height: 90vh; overflow-y: auto; background: rgba(15, 23, 42, 0.9); border: 1px solid var(--border-color); box-shadow: var(--shadow-xl); border-radius: 16px;">
            <div class="imagen-modal-header" style="border-bottom: 2px solid var(--color-primary); padding-bottom: 0.75rem; flex-shrink: 0; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 0.6rem;">
                    <span style="font-size: 1.75rem;">💼</span>
                    <div>
                        <h3 style="font-family: 'Outfit', sans-serif; font-weight: 800; margin: 0; color: var(--color-text-main);">Form FDA 2253 Transmittal Sheet</h3>
                        <p style="font-size: 0.68rem; color: var(--color-text-muted); margin: 0.15rem 0 0 0;">Transmittal of Advertisements and Promotional Labeling for Drugs and Biologics for Human Use</p>
                    </div>
                </div>
                <button class="imagen-modal-close" onclick="closeFda2253Modal()" style="background: none; border: none; color: var(--color-text-muted); font-size: 1.5rem; cursor: pointer; outline: none;">&times;</button>
            </div>
            
            <div class="imagen-modal-body" style="padding-top: 1.25rem; display: flex; flex-direction: column; gap: 1rem;">
                <!-- Official FDA Grid -->
                <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 0.75rem; border: 1px solid var(--border-color); border-radius: 8px; overflow: hidden; background: rgba(0,0,0,0.15); font-size: 0.68rem; border-left: 4px solid var(--color-primary);">
                    <!-- Left Block -->
                    <div style="display: flex; flex-direction: column; border-right: 1px solid var(--border-color);">
                        <!-- Box 1 -->
                        <div style="padding: 0.6rem; border-bottom: 1px solid var(--border-color); display: flex; flex-direction: column; gap: 0.25rem;">
                            <span style="font-weight: 800; text-transform: uppercase; font-size: 0.55rem; color: var(--color-primary);">1. APPLICANT NAME & ADDRESS</span>
                            <span id="fda-box1-name" style="font-weight: 700; color: var(--color-text-main);"></span>
                            <span id="fda-box1-address" style="color: var(--color-text-muted); line-height: 1.3;"></span>
                            <span id="fda-box1-tel" style="font-weight: 600; color: var(--color-text-muted);"></span>
                        </div>
                        <!-- Box 4 -->
                        <div style="padding: 0.6rem; display: flex; flex-direction: column; gap: 0.35rem;">
                            <span style="font-weight: 800; text-transform: uppercase; font-size: 0.55rem; color: var(--color-primary);">4. PRODUCT DESCRIPTION</span>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
                                <div style="display: flex; flex-direction: column; gap: 0.15rem;">
                                    <span style="font-size: 0.52rem; text-transform: uppercase; color: var(--color-text-muted);">Proprietary Name</span>
                                    <span id="fda-box4-proprietary" style="font-weight: 700; color: var(--color-text-main);"></span>
                                </div>
                                <div style="display: flex; flex-direction: column; gap: 0.15rem;">
                                    <span style="font-size: 0.52rem; text-transform: uppercase; color: var(--color-text-muted);">Established Name</span>
                                    <span id="fda-box4-established" style="font-weight: 600; color: var(--color-text-main); font-style: italic;"></span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Right Block -->
                    <div style="display: flex; flex-direction: column;">
                        <!-- Box 2 -->
                        <div style="padding: 0.6rem; border-bottom: 1px solid var(--border-color); display: flex; flex-direction: column; gap: 0.15rem;">
                            <span style="font-weight: 800; text-transform: uppercase; font-size: 0.55rem; color: var(--color-primary);">2. TRANSMITTAL DATE</span>
                            <span id="fda-box2-date" style="font-weight: 700; color: var(--color-text-main);"></span>
                        </div>
                        <!-- Box 3 -->
                        <div style="padding: 0.6rem; border-bottom: 1px solid var(--border-color); display: flex; flex-direction: column; gap: 0.15rem;">
                            <span style="font-weight: 800; text-transform: uppercase; font-size: 0.55rem; color: var(--color-primary);">3. BLA / NDA APPLICATION NO.</span>
                            <span id="fda-box3-appno" style="font-weight: 700; font-family: monospace; color: var(--color-text-main);"></span>
                        </div>
                        <!-- Box 5 -->
                        <div style="padding: 0.6rem; display: flex; flex-direction: column; gap: 0.15rem;">
                            <span style="font-weight: 800; text-transform: uppercase; font-size: 0.55rem; color: var(--color-primary);">5. SUBMISSION TYPE</span>
                            <span style="font-weight: 700; color: var(--color-text-main);">Original Submission (eCTD)</span>
                        </div>
                    </div>
                </div>
                
                <!-- Box 7 (Table of Materials) -->
                <div style="display: flex; flex-direction: column; border: 1px solid var(--border-color); border-radius: 8px; overflow: hidden; background: rgba(0,0,0,0.15); font-size: 0.68rem;">
                    <div style="padding: 0.5rem 0.6rem; border-bottom: 1px solid var(--border-color); background: rgba(255,255,255,0.02); font-weight: 800; text-transform: uppercase; font-size: 0.55rem; color: var(--color-primary);">
                        7. LIST OF COMPLIANCE MATERIALS BEAT-CHECKED & WATERMARKED
                    </div>
                    <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.65rem;">
                        <thead>
                            <tr style="border-bottom: 1px solid var(--border-color); background: rgba(0,0,0,0.2); font-weight: 700; color: var(--color-text-muted);">
                                <th style="padding: 0.5rem 0.6rem;">MATERIAL SUBJECT / TITLE</th>
                                <th style="padding: 0.5rem 0.6rem;">VEEVA PROMOMATS ID</th>
                                <th style="padding: 0.5rem 0.6rem;">TACTIC TYPE</th>
                                <th style="padding: 0.5rem 0.6rem; text-align: right;">CRYPTOGRAPHIC VERIFICATION SEAL</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: none;">
                                <td style="padding: 0.6rem; font-weight: 700; color: var(--color-text-main);" id="fda-box7-title"></td>
                                <td style="padding: 0.6rem; font-family: monospace; font-weight: 600; color: var(--color-text-main);" id="fda-box7-veevaid"></td>
                                <td style="padding: 0.6rem; color: var(--color-text-muted);" id="fda-box7-type"></td>
                                <td style="padding: 0.6rem; text-align: right; font-family: monospace; font-size: 0.58rem; color: var(--color-primary);" id="fda-box7-hash"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
                <!-- Box 8 (Signature Block) -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; border: 1px solid var(--border-color); border-radius: 8px; overflow: hidden; background: rgba(0,0,0,0.15); font-size: 0.68rem; padding: 0.6rem; border-left: 4px solid #10b981;">
                    <div style="display: flex; flex-direction: column; gap: 0.25rem;">
                        <span style="font-weight: 800; text-transform: uppercase; font-size: 0.55rem; color: #10b981;">8. DIGITAL SIGNATURE (APPLICANT SIGN-OFF)</span>
                        <span id="fda-box8-signature" style="font-family: 'Outfit', cursive, sans-serif; font-size: 1rem; font-weight: 700; color: #34d399; letter-spacing: 1px;"></span>
                        <span style="font-size: 0.52rem; color: var(--color-text-muted); text-transform: uppercase;">AUTHORIZED PHARMA REGULATORY AUDITOR</span>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 0.25rem; justify-content: flex-end; align-items: flex-end; text-align: right;">
                        <span style="font-size: 0.52rem; text-transform: uppercase; color: var(--color-text-muted);">Signature Sign-off Date</span>
                        <span id="fda-box8-date" style="font-weight: 700; color: var(--color-text-main);"></span>
                    </div>
                </div>
                
                <!-- Actions Row -->
                <div style="display: flex; justify-content: flex-end; gap: 0.5rem; border-top: 1px solid var(--border-color); padding-top: 0.75rem; margin-top: 0.5rem; flex-shrink: 0;">
                    <button class="btn btn-secondary" onclick="closeFda2253Modal()" style="padding: 0.45rem 1rem; font-size: 0.72rem; font-weight: 700; border-radius: 6px; cursor: pointer;">Cancel</button>
                    <button class="btn btn-primary" onclick="printFda2253Form()" style="padding: 0.45rem 1.25rem; font-size: 0.72rem; font-weight: 700; border-radius: 6px; cursor: pointer; display: flex; align-items: center; gap: 0.25rem; background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important; color: white !important; border: none;">
                        <span>🖨️ Export FDA 2253 Binder PDF</span>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- GOOGLE IMAGEN 3 ASSET CREATOR MODAL -->
    <div class="imagen-modal-overlay" id="imagen-modal">
        <div class="imagen-modal-card" style="background: rgba(15, 23, 42, 0.88); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid var(--border-color); box-shadow: var(--shadow-xl);">
            <div class="imagen-modal-header" style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 0.6rem;">
                    <span style="font-size: 1.75rem;">✨</span>
                    <div>
                        <h3 style="color: var(--color-text-main); font-weight: 800;">Google Imagen 3 Asset Creator</h3>
                        <p style="color: var(--color-text-muted);">AI-powered, brand-compliant clinical image generation</p>
                    </div>
                </div>
                <button class="imagen-modal-close" onclick="closeImagenModal()">&times;</button>
            </div>
            
            <div class="imagen-modal-body">
                <div class="imagen-form-group">
                    <label>Active Clinical Brand</label>
                    <select id="imagen-brand-select" class="imagen-select">
                        <option value="product_a">KEYTRUDA (Pembrolizumab)</option>
                        <option value="product_b">LENVIMA (Lenvatinib)</option>
                        <option value="product_c">WELIREG (Belzutifan)</option>
                    </select>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div class="imagen-form-group">
                        <label>Generative Model</label>
                        <select id="imagen-model-select" class="imagen-select">
                            <option value="imagen-3-clinical">Imagen 3 (Clinical High-Fidelity)</option>
                            <option value="imagen-3-diagram">Imagen 3 (Medical Biology)</option>
                            <option value="imagen-3-abstract">Imagen 3 (Abstract Brand Colors)</option>
                        </select>
                    </div>
                    <div class="imagen-form-group">
                        <label>Visual Style Preset</label>
                        <select id="imagen-style-select" class="imagen-select">
                            <option value="clinical-realism">Clinical Realism (Photorealistic)</option>
                            <option value="microbiology-3d">3D Cellular Illustration</option>
                            <option value="clean-infographic">Clean Vector Chart</option>
                        </select>
                    </div>
                </div>
                
                <div class="imagen-form-group">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
                        <label style="margin: 0;">Image Synthesis Prompt</label>
                        <select id="imagen-prompt-presets" class="imagen-select" style="width: auto; font-size: 0.6rem; padding: 0.1rem 0.3rem; height: auto; border-radius: 4px;">
                            <option value="">Prompt Presets...</option>
                            <option value="Doctor consulting with a patient in a modern oncology clinic, warm lighting, brand-compliant.">Oncology Consultation</option>
                            <option value="3D molecular model showing drug molecules binding to receptor cells, neon brand highlights.">Receptor Binding</option>
                            <option value="A diverse group of healthy seniors smiling outdoors, photorealistic, premium lighting.">Healthy Patients</option>
                        </select>
                    </div>
                    <textarea id="imagen-prompt-input" class="imagen-textarea" placeholder="e.g., Doctor consulting with a patient in a modern oncology clinic, warm lighting, brand-compliant, high-fidelity..."></textarea>
                </div>

                <div class="imagen-form-group">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
                        <label style="margin: 0;">Negative Prompt (Elements to Avoid)</label>
                        <select id="imagen-negative-presets" class="imagen-select" style="width: auto; font-size: 0.6rem; padding: 0.1rem 0.3rem; height: auto; border-radius: 4px;">
                            <option value="">Negative Presets...</option>
                            <option value="blurry, low resolution, deformed anatomy, text overlays, cartoonish, off-brand colors.">Clinical Safeguard (Strict)</option>
                            <option value="cartoon, illustration, dark lighting, depressing clinical environment.">Realism Safeguard</option>
                        </select>
                    </div>
                    <input type="text" id="imagen-negative-input" class="imagen-select" placeholder="e.g., blurry, low resolution, deformed anatomy..." value="blurry, low resolution, deformed anatomy, text overlays, cartoonish, off-brand colors.">
                </div>
                
                <div class="imagen-form-group" style="display: flex; align-items: center; justify-content: space-between; background: rgba(255,255,255,0.02); padding: 0.5rem 0.75rem; border-radius: 6px; border: 1px solid var(--border-color); margin-bottom: 1.25rem;">
                    <div style="display: flex; flex-direction: column; gap: 0.1rem;">
                        <span style="font-size: 0.7rem; font-weight: 700; color: var(--color-text-main);">Google SynthID Watermarking</span>
                        <span style="font-size: 0.58rem; color: var(--color-text-muted);">Injects an imperceptible digital watermark to prove clinical origin.</span>
                    </div>
                    <label class="switch-toggle" style="position: relative; display: inline-block; width: 34px; height: 20px;">
                        <input type="checkbox" id="imagen-synthid-toggle" checked style="opacity: 0; width: 0; height: 0;">
                        <span class="slider-round" style="position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: rgba(255,255,255,0.1); transition: .4s; border-radius: 20px;"></span>
                    </label>
                </div>
                
                <!-- Google Vibrant Gemini Gradient Generate Button -->
                <button class="btn btn-imagen-generate" id="btn-imagen-generate-run" onclick="generateImagenAsset()" style="width: 100%; display: flex; align-items: center; justify-content: center; gap: 0.5rem; position: relative;">
                    <span>✨ Generate High-Fidelity Clinical Imagery</span>
                    <span class="btn-spinner" id="imagen-spinner" style="display: none;"></span>
                </button>
            </div>
        </div>
    </div>

    <!-- IMMERSIVE CHAT PORTAL MODAL -->
    <div class="imagen-modal-overlay" id="expanded-chat-modal" style="display: none; justify-content: center; align-items: center; z-index: 10000; background: rgba(0, 0, 0, 0.6); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);">
        <div class="imagen-modal-card" style="max-width: 950px; width: 95%; height: 85vh; display: flex; flex-direction: column; background: rgba(15, 23, 42, 0.9); border: 1px solid var(--border-color); box-shadow: var(--shadow-xl); border-radius: 16px;">
            <div class="imagen-modal-header" style="border-bottom: 1px solid var(--border-color); padding-bottom: 0.6rem; flex-shrink: 0; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="font-size: 1.5rem;">💬</span>
                    <div>
                        <h3 style="font-family: 'Outfit', sans-serif; font-weight: 800; margin: 0; color: var(--color-text-main);">Immersive Conversational Chat Portal</h3>
                        <p style="font-size: 0.62rem; color: var(--color-text-muted); margin: 0.15rem 0 0 0;">Detailed clinical instruction routing and multi-agent orchestration logs</p>
                    </div>
                </div>
                <button class="imagen-modal-close" onclick="closeExpandedChat()" style="background: none; border: none; color: var(--color-text-muted); font-size: 1.5rem; cursor: pointer; outline: none;">&times;</button>
            </div>
            
            <div class="imagen-modal-body" style="flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 1rem; padding: 1rem 0 0 0;">
                <!-- Expanded chat history scroll area -->
                <div class="chat-messages" id="expanded-chat-body" style="flex: 1; overflow-y: auto; padding: 0.75rem 1rem; background: rgba(0,0,0,0.18); border-radius: 8px; border: 1px solid var(--border-color); display: flex; flex-direction: column; gap: 0.85rem;">
                    <!-- Synced bubbles go here -->
                </div>
                
                <!-- Form input bar -->
                <form class="chat-input-form" onsubmit="submitExpandedChat(event)" style="padding: 0.5rem 1rem !important; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface-solid); margin: 0 !important; flex-shrink: 0; display: flex; gap: 0.5rem; align-items: center; box-sizing: border-box; width: 100%;">
                    <input type="text" id="expanded-chat-input" placeholder="Enter detailed multi-agent orchestration instruction..." autocomplete="off" required style="font-size: 0.78rem !important; outline: none; flex: 1; background: transparent; border: none; color: var(--color-text-main);">
                    <div style="display: flex; gap: 0.4rem; align-items: center; flex-shrink: 0;">
                        <button type="button" class="btn btn-secondary btn-small" onclick="clearExpandedChat()" style="padding: 0.35rem 0.75rem; font-size: 0.65rem; font-weight: 700; border-radius: 6px; cursor: pointer;">Clear</button>
                        <button type="submit" class="btn btn-primary btn-small" style="padding: 0.35rem 0.85rem; font-size: 0.65rem; font-weight: 700; border-radius: 6px; cursor: pointer; background: var(--color-primary); color: white; border: none;">Send</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- IMMERSIVE CONSOLE LOG PORTAL MODAL -->
    <div class="imagen-modal-overlay" id="expanded-console-modal" style="display: none; justify-content: center; align-items: center; z-index: 10000; background: rgba(0, 0, 0, 0.6); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);">
        <div class="imagen-modal-card" style="max-width: 950px; width: 95%; height: 85vh; display: flex; flex-direction: column; background: rgba(15, 23, 42, 0.9); border: 1px solid var(--border-color); box-shadow: var(--shadow-xl); border-radius: 16px;">
            <div class="imagen-modal-header" style="border-bottom: 1px solid var(--border-color); padding-bottom: 0.6rem; flex-shrink: 0; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="font-size: 1.5rem;">🖥️</span>
                    <div>
                        <h3 style="font-family: 'Outfit', sans-serif; font-weight: 800; margin: 0; color: var(--color-text-main);">Immersive Master Orchestrator Console Logs</h3>
                        <p style="font-size: 0.62rem; color: var(--color-text-muted); margin: 0.15rem 0 0 0;">Real-time multi-agent self-healing, claims beat-checks, and compilation events</p>
                    </div>
                </div>
                <button class="imagen-modal-close" onclick="closeExpandedConsole()" style="background: none; border: none; color: var(--color-text-muted); font-size: 1.5rem; cursor: pointer; outline: none;">&times;</button>
            </div>
            
            <div class="imagen-modal-body" style="flex: 1; min-height: 0; display: flex; flex-direction: column; padding: 1rem 0 0 0;">
                <div class="console-body" id="expanded-console-body" style="flex: 1; overflow-y: auto; padding: 0.75rem 1rem; background: #070b19; border: 1px solid var(--border-color); border-radius: 8px; font-family: monospace; font-size: 0.68rem; line-height: 1.5; color: #34d399; box-shadow: inset 0 0 10px rgba(0,0,0,0.8); display: flex; flex-direction: column; gap: 0.35rem;">
                    <!-- Log history goes here -->
                </div>
            </div>
        </div>
    </div>
"""

# 3. Insert these modals right before the closing </body> tag
print("Stitching modals into index.html...")
closing_body_tag = "</body>"

if closing_body_tag in content:
    # Let's insert the modals right before the closing body tag
    content = content.replace(closing_body_tag, modals_html + "\n</body>")
    print("✅ Successfully stitched 5 high-fidelity modals into index.html!")
else:
    print("❌ Error: Closing </body> tag not found in index.html! Stitching failed.")

# 4. Save the updated file
with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
print("🎉 Success: index.html has been perfectly updated!")
