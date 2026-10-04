from flask import flash, render_template, redirect, url_for, session, Blueprint, request

auth = Blueprint("auth", __name__)


# main
@auth.route("/", methods=["GET"])
def main():
    return render_template("base.html")

# register
@auth.route("/register", methods=["POST", "GET"])
def register():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        session['username'] = username
        session['password'] = password
    return render_template("register.html") 

# login
@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username==session[username] and password==session[password]:
            return render_template('service.html')
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for('auth.login'))

# logout
@auth.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    flash("You have been logged out.", "success")
    return redirect(url_for('auth.login'))