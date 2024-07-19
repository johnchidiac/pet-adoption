"""Pet Adoption Application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import NewPetForm, EditPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False  # Disable redirect interception

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:Bu11fr09@localhost:5432/pet_adoption"
)
app.config["SECRET_KEY"] = "yomama"
app.config["SQLALCHEMY_ECHO"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

debug = DebugToolbarExtension(app)

connect_db(app)

with app.app_context():
    db.create_all()


@app.route("/")
def show_homepage():
    """Show homepage with list of pets."""

    pets = Pet.query.all()
    return render_template("index.jinja-html", pets=pets)


@app.route("/add/", methods=["GET", "POST"])
def add_pet():
    """Show form to add a pet and process it."""
    form = NewPetForm()
    if form.validate_on_submit():

        name = request.form["name"]
        species = request.form["species"]
        photo_url = request.form["photo_url"]
        age = request.form["age"]
        notes = request.form["notes"]

        new_pet = Pet(
            name=name, species=species, photo_url=photo_url, age=age, notes=notes
        )

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("add-pet-form.jinja-html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Show form to edit a pet and process it."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect("/")

    else:
        return render_template("pet-details.jinja-html", form=form, pet=pet)
