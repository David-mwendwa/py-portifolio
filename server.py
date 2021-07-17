from flask import Flask, render_template

app = Flask(__name__)
print(app)
print(__name__)

@app.route("/index.html")
def home():
  return render_template('index.html')

@app.route("/about.html")
def about():
  return render_template('about.html')

@app.route("/works.html")
def works():
  return render_template('works.html')

