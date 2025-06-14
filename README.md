# Portfolio Website

A Flask-based portfolio website showcasing skills, projects, and contact information.

## Deployment Instructions

### Render Deployment

1. Sign up for a free account at [Render](https://render.com/)

2. Create a New Web Service:

   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Choose the repository containing your portfolio

3. Configure the Web Service:

   - Name: portfolio-website (or your preferred name)
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Plan: Free

4. Set Environment Variables:

   - Click on "Environment" tab
   - Add the following variables:
     ```
     MAIL_USERNAME=your-email@gmail.com
     MAIL_PASSWORD=your-app-password
     ```

5. Deploy:
   - Click "Create Web Service"
   - Render will automatically deploy your application
   - Your site will be available at `https://your-app-name.onrender.com`

## Local Development

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a config.env file with your email settings:

```
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

4. Run the development server:

```bash
python app.py
```

## Features

- Responsive design
- Contact form with email functionality
- Skills showcase
- Project portfolio
- About section
- Social media links

## Technologies Used

- Flask
- Flask-Mail
- HTML5
- CSS3
- JavaScript
- Python-dotenv
- Gunicorn
