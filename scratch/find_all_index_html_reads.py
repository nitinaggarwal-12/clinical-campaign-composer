import json

transcript_path = "/Users/nitinagga/.gemini/jetski/brain/856f25a9-79fa-4567-afbd-abd0038341d5/.system_generated/logs/transcript.jsonl"

print("Scanning transcript for all index.html reads/writes...")

with open(transcript_path, "r", encoding="utf-8") as f:
    for line_idx, line in enumerate(f):
        try:
            step = json.loads(line)
            step_index = step.get("step_index", line_idx)
            step_type = step.get("type", "")
            content = step.get("content", "")
            
            # Check if this step is a tool call or response involving index.html
            is_index_html = False
            
            # Check tool calls in step
            for tc in step.get("tool_calls", []):
                args = tc.get("args", {})
                path = args.get("AbsolutePath", "") or args.get("TargetFile", "")
                if "index.html" in str(path):
                    is_index_html = True
                    
            # Check step content
            if "index.html" in content or "DOCTYPE html" in content:
                is_index_html = True
                
            if is_index_html:
                # Print summary of the step
                preview = content[:80].replace("\n", " ").strip()
                print(f"Step {step_index} | Type: {step_type} | Content Len: {len(content)} | Preview: {preview}...")
                
        except Exception as e:
            continue

print("Scan finished!")
