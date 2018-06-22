from flask import Flask
from flask import render_template
from flask import jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", title="Home")

@app.route('/hello/<name>')
def hello_there(name):
    from datetime import datetime
    now = datetime.now()
    content = "Hello there, " + name + "!"
    return render_template(
        "there.html",
        title ='Hello, Flask',
        content = content,
        date = now.strftime("%A, %d %B, %Y at %X")
    )

@app.route('/api/data')
def get_data():
  return app.send_static_file('data.json')

@app.route('/about')
def about():
        return render_template("about.html", title = "About us")

@app.route('/contact')
def contact():
        return render_template("contact.html", title = "Contact us")

# ajax
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)