
# voeg session lib toe
from flask import Flask, render_template, request, url_for, redirect, session, session

#1 permanent session instellen
from datetime import timedelta

from Flask_HTTP import app

app = Flask(__name__)
# secret key toevoegen voor toegang tot session-data
app.secret_key = "hello"

# 2 permanent session instellen
app.permanent_session_lifetime = timedelta(minutes=5)





@app.route("/")
def home():
    return render_template("index.html")

# maak een dictionary key en voeg toe aan lib session en koppel er de
# value 'user'aan
# 3 permanent session instellen
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

# check of de user bestaat in session en geef toegang met een return
#zo niet een else statement met een redirect naar de lgin-pagina
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

# een login-pagina maken en session data verwijderen bij uitloggen
# als we ingelogd zijn  bij @app.route("/login" if statement
# toevoegen met een redirect naar de user pagina
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
