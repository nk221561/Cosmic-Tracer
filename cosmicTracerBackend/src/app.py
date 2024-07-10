from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from service import CosmicTracerService
import base64
import random
from constellation_search import search_constellation_by_name
app = Flask(__name__)
CORS(app)

FRONTEND_DIR = "D:\\cosmicTracerFrontend"


TEMPLATE_DIR = "D:\\cosmicTracerBackend\\templates"
template_images = {
    "Orion": os.path.join(TEMPLATE_DIR, "orion.jpg"),
    "Ursa Major": os.path.join(TEMPLATE_DIR, "ursa_major.jpg"),
    "Leo": os.path.join(TEMPLATE_DIR, "leo.jpg"),
    "Aquarius": os.path.join(TEMPLATE_DIR, "aquarius.jpg"),
  
}

@app.route('/random-constellation', methods=['GET'])
def get_random_constellation():
    # Choose a random constellation from the list of available constellations
    random_constellation = random.choice(list(template_images.keys()))

    # Fetch information for the randomly selected constellation
    constellation_info = search_constellation_by_name(random_constellation)

    if constellation_info:
        return jsonify(constellation_info)
    else:
        return jsonify({"error": "Failed to fetch random constellation information"}), 500
 
    
@app.route('/search', methods=['POST'])
def search_constellation():
    # Get the name of the constellation from the request
    data = request.json
    constellation_name = data.get('constellation_name')

    # Call the search_constellation_by_name function to search for the constellation
    constellation_info = search_constellation_by_name(constellation_name)

    if constellation_info:
        return jsonify(constellation_info)
    else:
        return jsonify({"error": "Constellation not found"}), 404

@app.route('/')
def index():
    return send_from_directory(os.path.join(FRONTEND_DIR, 'index.html'))


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"})

        image_file = request.files['image']
        image_bytes = image_file.read()

        # Initialize variables to store matched constellation and image data
        matched_constellation = None
        image_data = None

        # Iterate through template images and compare with the uploaded image
        for constellation, template_path in template_images.items():
            print(f"Comparing with template: {template_path}")
            service = CosmicTracerService(template_path)
            result = service.identify_constellation(image_bytes)
            print(f"Result for {constellation}: {result}")
            if result["result"] == "Yes, this is a known constellation":
                matched_constellation = constellation
                with open(template_path, "rb") as image_file:
                    image_data = base64.b64encode(image_file.read()).decode('utf-8')
                break

        # Check if a matched constellation is found
        if matched_constellation:
            return jsonify({
                "result": f"Congratulations! This image matches {matched_constellation} constellation.",
                "type": "success",
                "constellation": matched_constellation,
                "image_data": image_data
            })
        else:
            return jsonify({"result": "Sorry, this image does not match any known constellation.", "type": "error"})
    else:
        return jsonify({"error": "Method not allowed"}), 405


if __name__ == '__main__':
    app.run(debug=True)
