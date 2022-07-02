from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/3832003")
def p3832003():
    return render_template("3832003.html")

@app.route("/4502226")
def p4502226():
    return render_template("4502226.html")

@app.route("/3832067")
def p3832067():
    return render_template("3832067.html")

@app.route("/4502382")
def p4502382():
    return render_template("4502382.html")