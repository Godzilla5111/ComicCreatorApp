# app/controller.py
import requests
import base64
from PIL import Image
import io

class ApiError(Exception):
    """Custom exception class to handle API errors."""
    pass

API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept": "image/png",
	"Authorization": "Bearer VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM",
	"Content-Type": "application/json"
}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as e:
        raise ApiError(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        raise ApiError(f"API request error: {e}")

def generate_comic_panel(text_inputs):
    images = []
    for text in text_inputs:
        if not text:
            continue
        try:
            image_bytes = query({"inputs": text})
            image = Image.open(io.BytesIO(image_bytes))
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            images.append(f"data:image/png;base64,{img_str}")
        except ApiError as e:
            raise e
        except Exception as e:
            raise ApiError(f"Error processing image: {e}")
    return images
