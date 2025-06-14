from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, send_from_directory
from flask_mail import Mail, Message
import os
import smtplib
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv('config.env')

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True
app.secret_key = 'your-secret-key-here'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching

# Email configuration
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER=os.getenv('MAIL_USERNAME'),
    MAIL_MAX_EMAILS=5,
    MAIL_ASCII_ATTACHMENTS=False,
    MAIL_DEBUG=True
)

# Log email configuration (without password)
logger.debug("Email Configuration:")
logger.debug(f"MAIL_SERVER: {app.config['MAIL_SERVER']}")
logger.debug(f"MAIL_PORT: {app.config['MAIL_PORT']}")
logger.debug(f"MAIL_USE_TLS: {app.config['MAIL_USE_TLS']}")
logger.debug(f"MAIL_USE_SSL: {app.config['MAIL_USE_SSL']}")
logger.debug(f"MAIL_USERNAME: {app.config['MAIL_USERNAME']}")
logger.debug(f"MAIL_PASSWORD is set: {bool(app.config['MAIL_PASSWORD'])}")

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Log the incoming request
        logger.debug("Received contact form submission")
        logger.debug(f"Form data: {request.form}")
        
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        # Log form data
        logger.debug(f"Name: {name}")
        logger.debug(f"Email: {email}")
        logger.debug(f"Message: {message}")
        
        # Validate form data
        if not all([name, email, message]):
            logger.error("Missing required fields")
            return jsonify({
                'success': False, 
                'error': 'All fields are required'
            }), 400
        
        # Validate email format
        if '@' not in email or '.' not in email:
            logger.error("Invalid email format")
            return jsonify({
                'success': False, 
                'error': 'Please enter a valid email address'
            }), 400
        
        # Validate email configuration
        if not app.config['MAIL_PASSWORD']:
            logger.error("Email password is not set")
            return jsonify({
                'success': False, 
                'error': 'Email configuration is not properly set up'
            }), 500
        
        # Create email message
        msg = Message(
            subject=f'New Contact Form Message from {name}',
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']]
        )
        
        msg.body = f"""
        New message from your website contact form:
        
        From: {name}
        Email: {email}
        
        Message:
        {message}
        """
        
        # Log email configuration
        logger.debug("Sending email with configuration:")
        logger.debug(f"SMTP Server: {app.config['MAIL_SERVER']}")
        logger.debug(f"SMTP Port: {app.config['MAIL_PORT']}")
        logger.debug(f"TLS: {app.config['MAIL_USE_TLS']}")
        logger.debug(f"SSL: {app.config['MAIL_USE_SSL']}")
        logger.debug(f"Username: {app.config['MAIL_USERNAME']}")
        
        # Send email
        try:
            logger.debug("Attempting to send email...")
            mail.send(msg)
            logger.info("Email sent successfully!")
            return jsonify({'success': True})
        except smtplib.SMTPAuthenticationError as e:
            logger.error(f"SMTP Authentication Error: {str(e)}")
            return jsonify({
                'success': False, 
                'error': 'Email authentication failed. Please check your email configuration.'
            }), 500
        except smtplib.SMTPException as e:
            logger.error(f"SMTP Error: {str(e)}")
            return jsonify({
                'success': False, 
                'error': 'Failed to send email. Please try again later.'
            }), 500
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({
            'success': False, 
            'error': 'An unexpected error occurred. Please try again later.'
        }), 500

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000) 