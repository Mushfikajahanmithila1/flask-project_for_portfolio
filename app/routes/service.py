from flask import flash, render_template, redirect, session, Blueprint, url_for, request
from app import db
from app.model import Service

services_bp = Blueprint("services", __name__)
# home directory
@services_bp.route("/services", methods=["GET"])
def view_services():
    if "username" not in session:
        return redirect(url_for("auth.register"))
    services = Service.query.all()
    return render_template("service.html", services=services)

# add directory
@services_bp.route("/add", methods=["POST"])
def add_service():
    if "username" not in session:
        return redirect(url_for("auth.register"))

    title = request.form.get("title")
    if title:
        new_service = Service(title=title)
        db.session.add(new_service)
        db.session.commit()
        flash("Service added successfully!", "success")
    return redirect(url_for("services.view_services"))

# toggle service
@services_bp.route("/toggle/<int:service_id>", methods=["POST"])
def toggle_status(service_id):
    service = Service.query.get(service_id)
    if service:
        if service.status == "Inactive":
            service.status = "Active"
        else:
            service.status = "Inactive"
        db.session.commit()
        return redirect(url_for("services.view_services"))

# clear service
@services_bp.route("/clear", methods=["POST"])
def clear_service():
    Service.query.delete()
    db.session.commit()
    flash("All services are cleared.", "info")
    return redirect(url_for("services.view_services"))