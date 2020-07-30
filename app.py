from flask import Flask
from flask import render_template, redirect, url_for

# -- Initialization --
app = Flask(__name__)


# -- Routes --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/redirect/one')
def redirect_one():
    # Works in deployment (using Heroku)
    # Works in CS .com
    # Fails in CS .dev
    return redirect('/success')


@app.route('/redirect/two')
def redirect_two():
    # Works in deployment
    # Works in CS .com
    # Fails in CS .dev
    return redirect(url_for('success'))


@app.route('/redirect/three')
def redirect_three():
    # Fails in deployment (obviously)
    # Fails in CS .com
    # Fails in CS .dev
    return redirect(f"http://0.0.0.0{url_for('success')}")


@app.route('/redirect/four')
def redirect_four():
    # Fails in deployment
    # Works in CS .com
    # Works in CS .dev
    return redirect(f"http://0.0.0.0:5000{url_for('success')}")


@app.route('/location')
def location():
    # Route to understand how the Location header is populated by Werkzeug
    # Show 302 body:
    success_redirect = redirect(url_for("success"))
    print(success_redirect.response)
    # Show 302 location header:
    headers = success_redirect.headers
    print(headers)
    return f"Location Header: {headers['Location']}"


@app.route('/success')
def success():
    # Note that the relative route of this <a> link works in all environments, including .dev
    return "Redirect Successful! <a href='/index'>home</a>"
