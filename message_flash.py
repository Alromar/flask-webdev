
# 1 voeg flash toe
from flask import Flask, render_template, request, url_for, redirect, session, session, flash


from datetime import timedelta

from Flask_HTTP import app

app = Flask(__name__)
app.secret_key = "hello"

app.permanent_session_lifetime = timedelta(minutes=5)





@app.route("/")
def home():
    return render_template("index.html")

# bericht bij login dat de user wordt herkend
# bericht dat de login succesvol is
# bericht dat de user al ingelogd is als hij nogmaals inlogt

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("login succesfull")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

# render nieuwe html template "user.html"
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user =user)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))

# flash bericht bij logout met popup naar login maken
# flash logout na check user in session
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
