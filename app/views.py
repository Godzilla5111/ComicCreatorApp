# # app/views.py
# from flask import Blueprint, render_template, request, jsonify
# from .controller import generate_comic_panel, ApiError

# app_routes = Blueprint('app_routes', __name__)

# @app_routes.route('/', methods=['GET', 'POST'])
# def index():
#     images = []
#     if request.method == 'POST':
#         try:
#             text_inputs = [request.form.get(f'text{i}') for i in range(1, 11)]
#             images = generate_comic_panel(text_inputs)
#         except ApiError as e:
#             return render_template('index.html', error=str(e), images=[])
#         except Exception as e:
#             return render_template('index.html', error="An unexpected error occurred.", images=[])
#     return render_template('index.html', images=images)

# app/views.py
from flask import Blueprint, render_template, request
from .controller import query, ApiError
from base64 import b64encode

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/', methods=['GET', 'POST'])
def index():
    image_data = []
    if request.method == 'POST':
        try:
            # Retrieve user input from the form
            text_inputs = [request.form.get(f'text{i}') for i in range(1, 11)]
            # Process each input to generate an image
            for input_text in text_inputs:
                if input_text:  # Only make API calls for non-empty inputs
                    image_bytes = query({"inputs": input_text})
                    encoded_image = "data:image/png;base64," + b64encode(image_bytes).decode('utf-8')
                    image_data.append(encoded_image)
        except ApiError as e:
            return render_template('index.html', error=str(e), image_data=None)
        except Exception as e:
            return render_template('index.html', error="An unexpected error occurred.", image_data=None)
    return render_template('index.html', image_data=image_data)



