"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from HeatherWhittleseyWebsite import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )



@app.route('/java')
def java():
    """Renders the java page."""
    return render_template(
        'java.html',
        title='Java',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/csharp')
def csharp():
    """Renders the csharp page."""
    return render_template(
        'csharp.html',
        title='Csharp',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/python')
def python():
    """Renders the python page."""
    return render_template(
        'python.html',
        title='Python',
        year=datetime.now().year,
        message='Your application description page.'
    )



@app.route('/web')
def web():
    """Renders the web page."""
    return render_template(
        'web.html',
        title='Web',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/net')
def net():
    """Renders the net page."""
    return render_template(
        'net.html',
        title='Net',
        year=datetime.now().year,
        message='Your application description page.'
    )
