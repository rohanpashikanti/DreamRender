from flask import Flask, request, render_template, send_file
from huggingface_hub import InferenceClient

app = Flask(__name__)

# Replace with your actual Hugging Face API token
api_token = "enter your api key here"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate-image", methods=["POST"])
def generate_image():
    prompt = request.form.get("prompt")
    client = InferenceClient(token=api_token)

    try:
        # Generate an image based on the prompt
        image = client.text_to_image(
            model="XLabs-AI/flux-RealismLora",
            prompt=prompt
        )

        # Save the image to a file
        image_path = "static/generated_image.png"
        image.save("/Users/rohanpashikanti/Downloads/ai-image-generator/static/images/i.png")

        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>AI Image Generator</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; margin: 50px; }}
                img {{ max-width: 100%; height: auto; border: 5px solid #6a11cb; border-radius: 20px; }}
                a {{ display: block; margin-top: 20px; text-decoration: none; font-size: 18px; color: #2575fc; }}
            </style>
        </head>
        <body>
            <h1>Your Generated Image</h1>
            <img src="{image_path}" alt="Generated Image">
            <a href="/">Generate Another Image</a>
        </body>
        </html>
        """
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
