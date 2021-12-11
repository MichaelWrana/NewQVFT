from qvft import app
from qvft import data
from flask import render_template


@app.route('/')
def index():
    return render_template('home.html',
                           navigation=data.nav_data,
                           partner_data=data.partner_data)


@app.route('/about/')
def about():
    return render_template('about.html',
                           navigation=data.nav_data)


@app.route('/team/')
def team():
    return render_template('team.html',
                           navigation=data.nav_data,
                           team_data=data.team_data)


@app.route('/sponsors/')
def sponsors():
    return render_template('sponsors.html',
                           navigation=data.nav_data)


@app.route('/hiring/')
def hiring():
    return render_template('hiring.html',
                           navigation=data.nav_data,
                           hiring_data=data.hiring_data)
