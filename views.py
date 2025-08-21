import os
import uuid
import numpy as np
from flask import request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

from . import app

# Load model
model = load_model(app.config['MODEL'])

# Load class names
CLASS_NAMES_FILE = os.path.join("application", "static", "models", "class_names.txt")
with open(CLASS_NAMES_FILE) as f:
    class_names = [line.strip() for line in f]

# Check file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def views():
    prediction_text = ''
    image_url = ''

    if request.method == 'POST':
        file = request.files.get('file')

        if file and allowed_file(file.filename):
            # Save image
            original_filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4().hex}_{original_filename}"
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(save_path)

            # Preprocess image
            img = image.load_img(save_path, target_size=(128, 128))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)

            # Predict
            prediction = model.predict(img_array)[0]
            predicted_index = np.argmax(prediction)
            predicted_class = class_names[predicted_index]
            confidence = prediction[predicted_index] * 100

            # Output
            prediction_text = f"Predicted Class: {predicted_class} ({confidence:.2f}%)"
            image_url = f"/static/uploads/{unique_filename}"
        else:
            prediction_text = "Invalid file. Please upload a .jpg or .png image."

    return render_template("index.html", prediction=prediction_text, image_path=image_url)