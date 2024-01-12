# https://www.youtube.com/watch?v=9MHYHgh4jYc&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=4

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello! this is the main page <h1>Hello</h1?>"

# @app.route("/<name>")
# def home(name):
#     return render_template("py.html", content=name, r=2)

@app.route("/")
def home():
    return render_template("py.html")

@app.route("/test")
def test():
    return render_template("newhtml.html")


if __name__=="__main__":
    app.run(debug=True)
# debug=True om niet de server opnieuw te hoeven starten bij iedere aanpassing