Potato Disease Classification Using AI/ML

Overview

This project is a smart and practical solution for detecting diseases in potato crops using artificial intelligence. Farmers and agricultural professionals can quickly identify leaf diseases, enabling timely intervention and better crop management.

The system leverages a convolutional neural network (CNN) trained on a diverse dataset of potato leaf images. The model predicts the type of disease—such as Late Blight, Early Blight, and Healthy Leaves—with high accuracy. To ensure reliable predictions, the training process includes class weighting to handle imbalanced datasets and improve performance across all disease classes.

The backend is built using Python and Flask, allowing users to upload an image of a potato leaf and receive instant predictions. The frontend displays the uploaded image alongside the predicted disease, making it intuitive and user-friendly.

This project demonstrates the power of AI in agriculture, bridging the gap between technology and farming. It can be expanded further with more disease classes, mobile compatibility, and enhanced accuracy using advanced models or transfer learning.

Features

Real-time image upload and disease prediction

Detects multiple potato diseases (Late Blight, Early Blight, Healthy, etc.)

Handles class imbalance using weighted training

Simple, user-friendly web interface

Technologies Used

Backend: Python, Flask

Machine Learning: TensorFlow / Keras, CNN

Frontend: HTML, CSS, JavaScript

Data Processing: NumPy, OpenCV, Pandas

Installation

Clone the repository:

git clone https://github.com/your-username/potato-disease-classifier.git
cd potato-disease-classifier


Install dependencies:

pip install -r requirements.txt


Run the Flask app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/

Usage

Open the web application.

Click Upload Image and select a potato leaf image.

The model predicts the disease and displays it next to the uploaded image.

Dataset

Curated potato leaf images organized by disease classes

Class weights applied during training for balanced predictions

Future Improvements

Add more potato disease types

Improve accuracy using transfer learning with pretrained models

Mobile compatibility for farmers in the field
