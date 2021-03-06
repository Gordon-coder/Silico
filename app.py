from flask import Flask, render_template

app = Flask(__name__)

# Index
@app.route("/")
def index():
    return render_template("index.html")

# Products
@app.route("/products/3832003")
def p3832003():
    return render_template("p3832003.html")

@app.route("/products/4502226")
def p4502226():
    return render_template("p4502226.html")

@app.route("/products/3832067")
def p3832067():
    return render_template("p3832067.html")

@app.route("/products/4502382")
def p4502382():
    return render_template("p4502382.html")

@app.route("/products/3832071")
def p3832071():
    return render_template("p3832071.html")

@app.route("/contents/336464")
def c336464():
    return render_template("c336464.html")

@app.route("/contents/793909a")
def c793909a():
    return render_template("c793909a.html")

@app.route("/contents/793909b")
def c793909b():
    return render_template("c793909b.html")

@app.route("/NewsDetail/2255002")
def nd2255002():
    return render_template("nd2255002.html")

@app.route("/NewsDetail/2254949")
def nd2254949():
    return render_template("nd2254949.html")