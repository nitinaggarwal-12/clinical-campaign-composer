import json

transcript_path = "/Users/nitinagga/.gemini/jetski/brain/856f25a9-79fa-4567-afbd-abd0038341d5/.system_generated/logs/transcript.jsonl"

search_terms = ["fda-2253", "imagen-modal", "detail-modal", "expanded-chat-modal", "expanded-console-modal"]

print("Running raw text scan of the transcript for modal IDs...")

matches = 0

with open(transcript_path, "r", encoding="utf-8") as f:
    for line_idx, line in enumerate(f):
        try:
            step = json.loads(line)
            step_index = step.get("step_index", line_idx)
            
            # Check if this step is from our current turn to avoid matching ourselves
            # (Our turn started around step 1390)
            if step_index >= 1390:
                continue
                
            raw_string = json.dumps(step)
            
            for term in search_terms:
                if term in raw_string:
                    matches += 1
                    print(f"\n🎯 MATCH FOUND at Step {step_index} (Line {line_idx}) for term '{term}':")
                    # Find where it is and print a snippet
                    pos = raw_string.find(term)
                    start_pos = max(0, pos - 150)
                    end_pos = min(len(raw_string), pos + 150)
                    snippet = raw_string[start_pos:end_pos]
                    print(f"   Snippet: ... {snippet.strip()} ...")
                    
        except Exception as e:
            continue

print(f"\nScan complete! Found {matches} matching occurrences before our turn.")
