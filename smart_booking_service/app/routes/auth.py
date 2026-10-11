from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth = Blueprint("auth", __name__)

# home
@auth.route("/")
@auth.route("/home")
def home():
    return render_template("index.html")

# register
@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if not username or not password:
            flash("Enter both username and password.", "error")
            return render_template("register.html")
        users = session.get("demo_users", {})
        if username in users:
            flash("That username is already registered in this browser session.", "error")
            return render_template("register.html")
        users[username] = password
        session["demo_users"] = users
        session["username"] = username
        flash("Registration successful!", "success")
        return redirect(url_for("auth.dashboard"))
    return render_template("register.html")

# login
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        users = session.get("demo_users", {})
        if username in users and users[username] == password:
            session["username"] = username
            flash("Login successful.", "success")
            return redirect(url_for("auth.dashboard"))
        flash("Invalid username or password. Register in this browser session first.", "error")
    return render_template("login.html")

# dashboard
@auth.route("/dashboard")
def dashboard():
    if "username" not in session:
        flash("Please log in first.", "error")
        return redirect(url_for("auth.login"))
    return render_template("dashboard.html", username=session["username"])

# logout
@auth.route("/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
