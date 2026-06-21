import json

transcript_path = "/Users/nitinagga/.gemini/jetski/brain/856f25a9-79fa-4567-afbd-abd0038341d5/.system_generated/logs/transcript.jsonl"

indices = []
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            indices.append(step.get("step_index", 0))
        except Exception:
            continue

if indices:
    print(f"Min step_index: {min(indices)}")
    print(f"Max step_index: {max(indices)}")
    print(f"Total steps: {len(indices)}")
    # Print the last 10 step indices
    print(f"Last 10 step indices: {indices[-10:]}")
else:
    print("No step indices found.")
