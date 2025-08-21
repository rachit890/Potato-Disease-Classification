from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import routes/views
from .views import views