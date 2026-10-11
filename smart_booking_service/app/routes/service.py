from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.model import Service

services_bp = Blueprint("services", __name__)

# logged_in check
def logged_in():
    if "username" not in session:
        flash("Please log in to manage services.", "error")
        return False
    return True

# services routes
@services_bp.route("/services")
def view_services():
    if not logged_in():
        return redirect(url_for("auth.login"))
    services = Service.query.order_by(Service.id.desc()).all()
    return render_template("service.html", services=services)

# service add
@services_bp.route("/services/add", methods=["POST"])
def add_service():
    if not logged_in():
        return redirect(url_for("auth.login"))
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    try:
        price = float(request.form.get("price", "0") or 0)
        if price < 0:
            raise ValueError
    except ValueError:
        flash("Price must be a valid non-negative number.", "error")
        return redirect(url_for("services.view_services"))
    if not title:
        flash("Service name is required.", "error")
        return redirect(url_for("services.view_services"))
    db.session.add(Service(title=title, description=description, price=price))
    db.session.commit()
    flash("Service added successfully.", "success")
    return redirect(url_for("services.view_services"))

# service toggle status
@services_bp.route("/services/<int:service_id>/toggle", methods=["POST"])
def toggle_status(service_id):
    if not logged_in():
        return redirect(url_for("auth.login"))
    service = db.session.get(Service, service_id)
    if service is None:
        flash("Service not found.", "error")
        return redirect(url_for("services.view_services"))
    service.status = "Inactive" if service.status == "Active" else "Active"
    db.session.commit()
    flash("Service status updated.", "success")
    return redirect(url_for("services.view_services"))

# service clear 
@services_bp.route("/services/clear", methods=["POST"])
def clear_service():
    if not logged_in():
        return redirect(url_for("auth.login"))
    Service.query.delete()
    db.session.commit()
    flash("All services cleared.", "info")
    return redirect(url_for("services.view_services"))

# service delete
@services_bp.route("/services/<int:service_id>/delete", methods=["POST"])
def delete_service(service_id):
    if not logged_in():
        return redirect(url_for("auth.login"))
    service = db.session.get(Service, service_id)
    if service:
        db.session.delete(service)
        db.session.commit()
        flash("Service deleted.", "success")
    return redirect(url_for("services.view_services"))
