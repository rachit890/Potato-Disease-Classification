import os

class Config:
    # Path to the saved model file
    MODEL_PATH = os.path.join("application", "static", "models")
    MODEL = os.path.join(MODEL_PATH, "model_v1.keras")

    # Folder to store uploaded images
    UPLOAD_FOLDER = os.path.join("application", "static", "uploads")
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}