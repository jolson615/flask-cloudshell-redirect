from flask import Flask
from flask import render_template, redirect, url_for


# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    data = {}
    redirects_list = [
        {'function':'redirect_one', 
        'description':"redirect('/index')",
        'color':'bg-danger'},
        {'function':'redirect_two', 
        'description':"redirect(f'''http://0.0.0.0:5000{url_for('index')}''')",
        'color':'bg-success'},
        {'function':'redirect_three', 
        'description':"redirect(f'''http://0.0.0.0{url_for('index')}''')",
        'color':'bg-danger'},
    ]
    data['redirects_list']=redirects_list
    return render_template('index.html', data=data)

@app.route('/redirect/one')
def redirect_one():
    return redirect('/index')

@app.route('/redirect/two')
def redirect_two():
    return redirect(f"http://0.0.0.0:5000{url_for('index')}")

@app.route('/redirect/three')
def redirect_three():
    return redirect(f"http://0.0.0.0{url_for('index')}")