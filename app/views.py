# app/views.py
# from flask import Blueprint, render_template, request
# from .controller import query, ApiError
# from base64 import b64encode

# # Create a Blueprint instance for app routes
# app_routes = Blueprint('app_routes', __name__)

# @app_routes.route('/', methods=['GET', 'POST'])
# def index():
#     image_data = []
#     if request.method == 'POST':
#         try:
#             # Retrieve user input from the form
#             text_inputs = [request.form.get(f'text{i}') for i in range(1, 11)]
#             # Process each input to generate an image
#             for input_text in text_inputs:
#                 if input_text:  # Only make API calls for non-empty inputs
#                     image_bytes = query({"inputs": input_text})
#                     encoded_image = "data:image/png;base64," + b64encode(image_bytes).decode('utf-8')
#                     image_data.append(encoded_image)
#         except ApiError as e:
#             return render_template('index.html', error=str(e), image_data=None)
#         except Exception as e:
#             return render_template('index.html', error="An unexpected error occurred.", image_data=None)
    
#     # If it's a GET request or no images are generated, just render the page
#     return render_template('index.html', image_data=image_data)


from flask import Blueprint, render_template, request, jsonify
from .controller import query, ApiError
from base64 import b64encode
from . import limiter

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/', methods=['GET', 'POST'])
@limiter.limit("30 per hour")
def index():
    if request.method == 'POST':
        image_data = []
        try:
            # Retrieve user input from the form
            text_inputs = [request.form.get(f'text{i}') for i in range(1, 11)]
            # Process each input to generate an image
            for input_text in text_inputs:
                if input_text:  # Only make API calls for non-empty inputs
                    image_bytes = query({"inputs": input_text})
                    encoded_image = "data:image/png;base64," + b64encode(image_bytes).decode('utf-8')
                    image_data.append(encoded_image)
            # Return a JSON response with the image data
            return jsonify({'image_data': image_data})
        except ApiError as e:
            return jsonify({'error': str(e)}), 500
        except Exception as e:
            return jsonify({'error': "An unexpected error occurred."}), 500
    # For a GET request, render the page normally
    return render_template('index.html', image_data=[])






