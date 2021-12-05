from qvft import app
from flask import render_template

#Generate Navigation

#EVERYTHING
#PAGE
navigation = [
    {
        "caption": "What We Do",
        "href": "/about"
    },
    {
        "caption": "Our Team",
        "href": "/team"
    },
    {
        "caption": "Sponsorship",
        "href": "/sponsors"
    },
    {
        "caption": "Hiring",
        "href": "/hiring"
    }
]

@app.route('/')
def index():
    return render_template('home.html', navigation=navigation)

@app.route('/about/')
def about():
    return render_template('about.html', navigation=navigation)

@app.route('/team/')
def team():
    return render_template('team.html', navigation=navigation)

@app.route('/sponsors/')
def sponsors():
    return render_template('sponsors.html', navigation=navigation)

@app.route('/hiring/')
def hiring():
    return render_template('hiring.html', navigation=navigation)