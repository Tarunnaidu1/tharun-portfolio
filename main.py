from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Contact Form Submission:\nName: {name}\nEmail: {email}\nMessage: {message}")
        return render_template('index.html', submitted=True)
    return render_template('index.html', submitted=False)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Contact Form Submission:\nName: {name}\nEmail: {email}\nMessage: {message}")
        return render_template('contact.html', submitted=True)
    return render_template('contact.html', submitted=False)

if __name__ == '__main__':
    app.run(debug=True) 