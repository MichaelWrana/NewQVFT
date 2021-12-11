from qvft import app
from flask import render_template

navigation_data = [
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

team_data = [
    {
        "name": "Patrick Singal",
        "role": "Manager",
        "url": "patrick.webp"
    },
    {
        "name": "Chris Molloy",
        "role": "Database Developer",
        "url": "chris.webp"
    },
    {
        "name": "Iain Headrick",
        "role": "Mechanical Designer",
        "url": "iain.webp"
    },
    {
        "name": "Julia Mackey",
        "role": "Business Operations",
        "url": "julia.webp"
    },
    {
        "name": "Ryan Power",
        "role": "Hardware Designer",
        "url": "ryan.webp"
    },
    {
        "name": "Elissa Wong",
        "role": "Plant Science Researcher",
        "url": "elissa.webp"
    },
    {
        "name": "Michael Wrana",
        "role": "Front-End Developer",
        "url": "wrana.webp"
    },
    {
        "name": "Donal Lynagh",
        "role": "Business Operations",
        "url": "donal.webp"
    },
    {
        "name": "Justine Kuczera",
        "role": "Business Operations",
        "url": "justine.webp"
    },
    {
        "name": "Quantum Hu",
        "role": "Hardware Designer",
        "url": "quantum.webp"
    },
    {
        "name": "Carter Conboy",
        "role": "Front-End Developer",
        "url": "carter.webp"
    },
    {
        "name": "Joshua Sass-Gregoire",
        "role": "Mechanical Designer",
        "url": "joshua.webp"
    },
]

partner_data = [
    {
        "url": "https://www.bmahydroponics.com/",
        "img": "bma.webp"
    },
    {
        "url": "https://zipgrow.com/",
        "img": "zipgrow.webp"
    },
    {
        "url": "https://www.igrow.news/",
        "img": "igrow.webp"
    },
    {
        "url": "https://www.engsoc.queensu.ca/get-involved/clubs/",
        "img": "engsoc.webp"
    },
    {
        "url": "http://simbl.ca/",
        "img": "simbl.webp"
    },
    {
        "url": "https://aerok.ca/",
        "img": "aerok.webp"
    },
]

@app.route('/')
def index():
    return render_template('home.html', navigation=navigation_data, partner_data=partner_data)


@app.route('/about/')
def about():
    return render_template('about.html', navigation=navigation_data)


@app.route('/team/')
def team():
    return render_template('team.html', navigation=navigation_data, team_data=team_data)


@app.route('/sponsors/')
def sponsors():
    return render_template('sponsors.html', navigation=navigation_data)


@app.route('/hiring/')
def hiring():
    return render_template('hiring.html', navigation=navigation_data)
