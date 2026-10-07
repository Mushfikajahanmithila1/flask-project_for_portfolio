from app import db


class Service(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.String(200),
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="active",
        nullable=False
    )