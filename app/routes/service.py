from flask import redirect, request, url_for, session, flash, render_template, Blueprint
from app import db
from app.model import Service

service_bp = Blueprint("service", __name__)

# view services
@service_bp.route("/services", methods=["GET"])
def view_services():
    if 'username' not in session:
        flash("Please log in to access the services.", "error")
        return redirect(url_for('auth.login'))
    services = Service.query.all()
    return render_template("service.html", services=services)

# add services
@service_bp.route("/add_service", methods=["POST", "GET"])
def add_service():
    if 'username' not in session:
        flash("Please log in to add a service.", "error")
        return redirect(url_for('auth.login'))
    
    if request.method == "POST":
        name = request.form.get("service_name")
        description = request.form.get("service_description")
        price = request.form.get("service_price")

        new_service = Service(name=name, description=description, price=price)
        db.session.add(new_service)
        db.session.commit()
        flash("Service added successfully!", "success")
        return redirect(url_for('service.view_services'))

# clear service
@service_bp.route("/delete_service/<int:service_id>", methods=["POST"])
def delete_service(service_id):
    if "username" not in session:
        flash("Please log in to delete a service.", "error")
        return redirect(url_for("auth.login"))

    service = Service.query.get_or_404(service_id)

    db.session.delete(service)
    db.session.commit()

    flash("Service deleted successfully!", "success")
    return redirect(url_for("service.view_services"))