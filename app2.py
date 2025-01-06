# api_key = "enter your api key here"
import requests
from huggingface_hub import InferenceClient

# Replace with your actual Hugging Face API token
api_token = "enter your api key here"

# Initialize the Inference Client
client = InferenceClient(token=api_token)

# Generate an image based on a text prompt
image = client.text_to_image(
    model="XLabs-AI/flux-RealismLora",
    prompt="pm modi drinking tea with ironman in cafe"
)
# Save the generated image

image.save("/Users/rohanpashikanti/Downloads/ai-image-generator/static/images/f.png")