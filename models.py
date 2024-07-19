from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()


def connect_db(app):
    db.init_app(app)


class Pet(db.Model):
    """Pet for adoption."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    species = db.Column(db.String(30), nullable=False)
    photo_url = db.Column(
        db.Text,
        default="https://thumbs.dreamstime.com/z/stylish-adorable-dogs-cats-posing-cute-pets-happy-different-purebred-puppies-cats-art-collage-isolated-multicolored-197575524.jpg",
    )
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
