import json
import re

transcript_path = "/Users/nitinagga/.gemini/jetski/brain/856f25a9-79fa-4567-afbd-abd0038341d5/.system_generated/logs/transcript.jsonl"
output_path = "/Users/nitinagga/Documents/Maestro-Automated-Claims-Harvesting-&-Trigger-Pipeline/frontend/index.html.original"

print("Searching the very beginning of the transcript for pristine index.html...")

original_html = None

with open(transcript_path, "r", encoding="utf-8") as f:
    for line_idx, line in enumerate(f):
        try:
            step = json.loads(line)
            step_index = step.get("step_index", line_idx)
            step_type = step.get("type", "")
            
            # We are looking for a VIEW_FILE tool call on index.html in the early steps
            is_view_of_index = False
            
            # Check tool calls
            for tc in step.get("tool_calls", []):
                args = tc.get("args", {})
                path = args.get("AbsolutePath", "")
                if "index.html" in str(path) and "style.css" not in str(path):
                    is_view_of_index = True
            
            # Also check step type and content
            content = step.get("content", "")
            if is_view_of_index or ("view_file" in step_type.lower() and "index.html" in content):
                # Let's extract the file content from this step!
                # In Antigravity transcripts, the tool result is typically in the content of the step,
                # or in the next step's response. Let's look for a large string starting with "<!DOCTYPE html>"
                # in the content, or search for it.
                pass
            
            # Search for the raw HTML in the content string
            if "<!DOCTYPE html>" in content and "html" in content:
                # Let's verify it's the original index.html
                # The original index.html had a header nav and tab buttons like "Marketing Workbench"
                if "Marketing Workbench" in content and "tab-workbench" in content:
                    print(f"✅ Found pristine index.html in step {step_index}! (Length: {len(content)} chars)")
                    original_html = content
                    break
                    
        except Exception as e:
            continue

if original_html:
    # Strip markdown code blocks if present
    if original_html.startswith("```html"):
        original_html = original_html[7:]
    elif original_html.startswith("```"):
        original_html = original_html[3:]
        
    if original_html.endswith("```"):
        original_html = original_html[:-3]
        
    original_html = original_html.strip()
    
    # Let's clean up line number prefixes if the agent viewed it with line numbers
    # Line numbers are usually in the format "12: <content>"
    lines = original_html.split("\n")
    cleaned_lines = []
    has_line_numbers = False
    
    # Check if first few lines have line number patterns like "1: <" or "2: <"
    for idx in range(min(5, len(lines))):
        if re.match(r"^\s*\d+:\s", lines[idx]):
            has_line_numbers = True
            break
            
    if has_line_numbers:
        print("🧹 Striping line numbers from recovered HTML...")
        for l in lines:
            cleaned_l = re.sub(r"^\s*\d+:\s", "", l)
            cleaned_lines.append(cleaned_l)
        original_html = "\n".join(cleaned_lines)
        
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(original_html)
    print(f"🎉 SUCCESS: Written pristine original index.html to: {output_path}")
else:
    print("❌ Could not find pristine HTML in the transcript. Running fallback search...")
