import sys
import os

# Add your project directory to the sys.path
path = '/home/yourusername/yourproject'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['FLASK_APP'] = 'app.py'
os.environ['FLASK_ENV'] = 'production'

# Import your Flask app
from app import app as application 