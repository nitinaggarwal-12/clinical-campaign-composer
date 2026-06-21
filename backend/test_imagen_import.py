import os
import sys

print("Checking Vertex AI imports...")
try:
    import vertexai
    from vertexai.preview.vision_models import ImageGenerationModel
    print("SUCCESS: Successfully imported ImageGenerationModel from vertexai.preview.vision_models!")
except Exception as e1:
    print("Preview vision models import failed:", e1)
    try:
        from vertexai.vision_models import ImageGenerationModel
        print("SUCCESS: Successfully imported ImageGenerationModel from vertexai.vision_models!")
    except Exception as e2:
        print("Standard vision models import failed:", e2)
        print("FAILED: Could not import ImageGenerationModel.")
        sys.exit(1)

print("Imports verified successfully.")
sys.exit(0)
