import os
import re

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    user_guide_path = os.path.join(base_dir, "frontend", "user_guide.html")
    
    with open(user_guide_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Locate the first mxgraph div block
    # We want to replace the first occurrence of data-mxgraph="..." with data-mxgraph="__BASELINE_DIAGRAM_JSON__"
    # To be extremely precise, let's match the first div containing the class "mxgraph" and replace its data-mxgraph attribute
    
    pattern = r'(<div class="mxgraph" style="max-width:100%; height: 100%; border:none; box-sizing:border-box;" data-mxgraph=")(.*?)(">)'
    
    # We only want to replace the FIRST occurrence (the baseline diagram)
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # Perform the replacement for the first occurrence only
        first_part = content[:match.start()]
        replacement = match.group(1) + "__BASELINE_DIAGRAM_JSON__" + match.group(3)
        second_part = content[match.end():]
        new_content = first_part + replacement + second_part
        
        with open(user_guide_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ Successfully injected __BASELINE_DIAGRAM_JSON__ placeholder into user_guide.html!")
    else:
        print("❌ Error: First mxgraph container not found.")

if __name__ == "__main__":
    main()
