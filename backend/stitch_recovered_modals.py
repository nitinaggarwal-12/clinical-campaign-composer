import os
import re

html_path = "/Users/nitinagga/Documents/Maestro-Automated-Claims-Harvesting-&-Trigger-Pipeline/frontend/index.html"
scratch_dir = "/Users/nitinagga/.gemini/jetski/brain/856f25a9-79fa-4567-afbd-abd0038341d5/scratch"

print("Stitching recovered modals into index.html...")

def extract_balanced_div(content, target_id):
    # Find start of div containing id="target_id" or id='target_id' or id=\"target_id\"
    pos = -1
    for quote in ['"', "'", '\\"']:
        marker = f'id={quote}{target_id}{quote}'
        pos = content.find(marker)
        if pos != -1:
            break
            
    if pos == -1:
        return None
        
    # Go backwards to find the opening <div
    start_div = content.rfind("<div", 0, pos)
    if start_div == -1:
        return None
        
    # Count tags to find the matching closing </div>
    count = 0
    idx = start_div
    while idx < len(content):
        if content[idx:idx+4] == "<div":
            count += 1
            idx += 4
        elif content[idx:idx+6] == "</div>":
            count -= 1
            idx += 6
            if count == 0:
                return content[start_div:idx]
        else:
            idx += 1
            
    return None

# Load the recovered files
modals = {}
for key in ["detail_modal", "fda_modal", "imagen_modal", "expanded_chat", "expanded_console"]:
    file_path = os.path.join(scratch_dir, f"recovered_{key}.html")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            raw_content = f.read()
            
        # Extract balanced div
        # The ID markers
        target_ids = {
            "detail_modal": "detail-modal",
            "fda_modal": "fda-2253-modal-overlay",
            "imagen_modal": "imagen-modal",
            "expanded_chat": "expanded-chat-modal",
            "expanded_console": "expanded-console-modal"
        }
        
        extracted = extract_balanced_div(raw_content, target_ids[key])
        if extracted:
            print(f"✅ Extracted balanced HTML for {key} ({len(extracted)} bytes)")
            modals[key] = extracted
        else:
            print(f"❌ Failed to extract balanced HTML for {key}")

# Read current index.html
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Stitching target modals right before the closing </body>
modals_html = "\n\n    <!-- ========================================== -->\n    <!-- 🛡️ RECOVERED SYSTEM MODALS & OVERLAYS -->\n    <!-- ========================================== -->\n"
for key, val in modals.items():
    modals_html += val + "\n\n"

# Add the network node tooltip and hidden triggers
modals_html += """    <!-- Real-Time Grounded Metadata Tooltip Card -->
    <div id="network-node-tooltip" class="network-tooltip" style="display: none; position: fixed; z-index: 9999; width: 280px; padding: 0.85rem; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-surface-solid); font-size: 0.7rem; box-shadow: var(--shadow-lg); pointer-events: none; line-height: 1.4; box-sizing: border-box; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);"></div>
"""

# Let's perform surgical replacements in the HTML body to align IDs:
# 1. Rename governance-ledger-network to claims-network-container
html_content = html_content.replace(
    'id="governance-ledger-network"',
    'id="claims-network-container"'
)

# 2. Add explorer active label tag and run integrity audit button inside Phase 3 center column so JS can bind to them!
# We will place them right next to the Claims Relationship Visualizer header in Phase 3!
claims_header_pattern = """<!-- Claims Relationship Visualizer Title -->
                                    <div style="display: flex; justify-content: space-between; align-items: center; flex-shrink: 0;">
                                        <span style="font-size: 0.72rem; font-weight: 800; color: var(--color-text-main); text-transform: uppercase; letter-spacing: 0.5px;">Claims Relationship Visualizer</span>"""

claims_header_replacement = """<!-- Claims Relationship Visualizer Title -->
                                    <div style="display: flex; justify-content: space-between; align-items: center; flex-shrink: 0; gap: 0.5rem;">
                                        <span style="font-size: 0.72rem; font-weight: 800; color: var(--color-text-main); text-transform: uppercase; letter-spacing: 0.5px;">Claims Relationship Visualizer</span>
                                        <span class="badge badge-active-label" id="explorer-active-label-tag" style="font-size: 0.55rem; background: var(--bg-surface-solid); border: 1px solid var(--border-color); padding: 0.15rem 0.4rem; border-radius: 4px; font-weight: 800; display: none;">Active: Week 24 Label</span>
                                        <button class="btn btn-primary btn-small" id="btn-visualizer-audit" onclick="triggerVisualizerScan()" style="display: none; align-items: center; gap: 0.25rem; font-size: 0.58rem; padding: 0.15rem 0.4rem;">
                                            <span>⚡</span> Run Integrity Audit
                                        </button>"""

html_content = html_content.replace(claims_header_pattern, claims_header_replacement)

# 3. Rename certificate modal IDs to match JS queries:
# - Rename modal-compliance-certificate to compliance-modal
# - Rename cert-timestamp to cert-time
# - Rename cert-medication to cert-med
html_content = html_content.replace('id="modal-compliance-certificate"', 'id="compliance-modal"')
html_content = html_content.replace('id="cert-timestamp"', 'id="cert-time"')
html_content = html_content.replace('id="cert-medication"', 'id="cert-med"')

# Stitch everything before </body>
if "<!-- 🛡️ RECOVERED SYSTEM MODALS & OVERLAYS -->" in html_content:
    # Clean old ones first
    parts = html_content.split("<!-- 🛡️ RECOVERED SYSTEM MODALS & OVERLAYS -->")
    html_content = parts[0] + "</body>\n</html>"

html_content = html_content.replace("</body>", modals_html + "</body>")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("SUCCESS: Surgically extracted, aligned, and stitched all recovered modals into index.html!")
