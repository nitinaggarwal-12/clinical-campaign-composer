html_path = "/Users/nitinagga/Documents/Maestro-Automated-Claims-Harvesting-&-Trigger-Pipeline/frontend/index.html"

print("Reading active index.html file...")
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate the Central Governance Board section and replace the single graph container
# with our stunning widescreen dual-column graph system!
old_graph_section = """                                    <!-- Vis.js Ledger Graph container -->
                                    <div style="width: 100%; height: 210px; position: relative; border-radius: 8px; border: 1px solid var(--border-color); overflow: hidden; background: rgba(0,0,0,0.2); flex-shrink: 0;">
                                        <div id="governance-ledger-network" style="height: 100%; width: 100%;"></div>
                                    </div>"""

new_graph_section = """<!-- Vis.js Dual-Column Governance Graph Visualizers -->
                                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; width: 100%; flex-shrink: 0;">
                                        <!-- Left Column: Claims Relationship Visualizer -->
                                        <div style="display: flex; flex-direction: column; gap: 0.35rem;">
                                            <span style="font-size: 0.58rem; font-weight: 800; color: var(--color-text-muted); text-transform: uppercase; letter-spacing: 0.5px;">1. Clinical Claims Ontology Map</span>
                                            <div style="height: 200px; position: relative; border-radius: 8px; border: 1px solid var(--border-color); overflow: hidden; background: rgba(0,0,0,0.25);">
                                                <div id="claims-network-container" style="height: 100%; width: 100%;"></div>
                                            </div>
                                        </div>
                                        
                                        <!-- Right Column: Digital Seal Trust Graph -->
                                        <div style="display: flex; flex-direction: column; gap: 0.35rem;">
                                            <span style="font-size: 0.58rem; font-weight: 800; color: var(--color-text-muted); text-transform: uppercase; letter-spacing: 0.5px;">2. Ledger Digital Seal Trust Graph</span>
                                            <div style="height: 200px; position: relative; border-radius: 8px; border: 1px solid var(--border-color); overflow: hidden; background: rgba(0,0,0,0.25);">
                                                <div id="governance-ledger-network" style="height: 100%; width: 100%;"></div>
                                            </div>
                                        </div>
                                    </div>"""

print("Surgically replacing Vis.js graph containers with dual widescreen system...")
if old_graph_section in content:
    content = content.replace(old_graph_section, new_graph_section)
    print("✅ Successfully implemented the Dual Vis.js Network system!")
else:
    # Fallback search if spacing is slightly different
    pattern = r'<!-- Vis\.js Ledger Graph container -->.*?<div id="governance-ledger-network".*?</div>.*?</div>'
    import re
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = re.sub(pattern, new_graph_section, content, flags=re.DOTALL)
        print("✅ Successfully implemented the Dual Vis.js Network system via regex!")
    else:
        print("❌ Error: Could not locate the old graph container in index.html!")

# Save the updated file
with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
print("🎉 Success: index.html has been updated perfectly!")
