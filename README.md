# Personal Portfolio Website

A modern, responsive personal portfolio website built with Flask, featuring a clean and elegant design.

## Features

- Responsive design that works on all devices
- Modern UI with smooth animations
- Interactive skill cards
- Contact form with backend processing
- Project showcase
- Social media integration

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python main.py
   ```
6. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
portfolio/
├── main.py
├── requirements.txt
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── about.html
    ├── skills.html
    ├── projects.html
    └── contact.html
```

## Technologies Used

- Flask (Backend)
- HTML5
- CSS3
- Font Awesome (Icons)
- Google Fonts
