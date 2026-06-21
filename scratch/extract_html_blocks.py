import json
import os

transcript_path = "/Users/nitinagga/.gemini/jetski/brain/856f25a9-79fa-4567-afbd-abd0038341d5/.system_generated/logs/transcript.jsonl"

targets = {
    "fda_modal": "fda-2253-modal-overlay",
    "imagen_modal": "imagen-modal",
    "expanded_chat": "expanded-chat-modal",
    "expanded_console": "expanded-console-modal",
    "detail_modal": "detail-modal"
}

print("Scanning transcript for original modals (step_index < 1320)...")

with open(transcript_path, "r", encoding="utf-8") as f:
    for line_idx, line in enumerate(f):
        try:
            step = json.loads(line)
            step_index = step.get("step_index", 0)
            
            # CRITICAL: Only match steps from the previous session to avoid self-referential loops!
            if step_index >= 1320:
                continue
                
            content = step.get("content", "")
            
            # Include tool call arguments
            for tc in step.get("tool_calls", []):
                for arg_val in tc.get("args", {}).values():
                    if isinstance(arg_val, str):
                        content += "\n" + arg_val
            
            # Check for each target using precise quote matching
            for key, marker in list(targets.items()):
                found_marker = False
                matched_pos = -1
                
                for quote in ['"', "'", '\\"']:
                    pattern = f'id={quote}{marker}{quote}'
                    if pattern in content:
                        found_marker = True
                        matched_pos = content.find(pattern)
                        break
                
                if found_marker:
                    # Found! Let's extract the block
                    start_pos = content.rfind("<div", 0, matched_pos)
                    if start_pos == -1:
                        start_pos = matched_pos - 50 # Fallback
                    
                    # Extract a large chunk (8500 chars) to cover the entire modal structure
                    block = content[start_pos : start_pos + 8500]
                    
                    # Clean up JSON escaping
                    block_clean = block.replace('\\"', '"').replace('\\n', '\n').replace('\\/', '/')
                    
                    if len(block_clean) > 300:
                        print(f"✅ Successfully extracted original HTML for {key} in step {step_index}! ({len(block_clean)} bytes)")
                        
                        output_file = f"/Users/nitinagga/.gemini/jetski/brain/856f25a9-79fa-4567-afbd-abd0038341d5/scratch/recovered_{key}.html"
                        with open(output_file, "w", encoding="utf-8") as out:
                            out.write(block_clean)
                        
                        # Remove from targets so we don't overwrite with a worse match
                        del targets[key]
                    
        except Exception as e:
            continue

print("Precise extraction process finished!")
