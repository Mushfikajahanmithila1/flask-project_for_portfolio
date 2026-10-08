from flask import flash, render_template, redirect, url_for, session, Blueprint, request

auth = Blueprint("auth", __name__)


# main
@auth.route("/home", methods=["GET"])
def home():
    return render_template("index.html")

# register
@auth.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        session["username"] = username
        session["password"] = password

        flash("Registration successful!", "success")

        return redirect(url_for("auth.home"))

    return render_template("register.html")
# login
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if (
            username == session.get("username")
            and password == session.get("password")
        ):
            flash("Login successful!", "success")
            return render_template("service.html")

        flash("Invalid username or password", "error")
        return redirect(url_for("auth.login"))

    return render_template("login.html")

# logout
@auth.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    flash("You have been logged out.", "success")
    return redirect(url_for('auth.login'))