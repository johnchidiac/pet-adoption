"""Forms for the application."""

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    BooleanField,
    ValidationError,
    TextAreaField,
    HiddenField,
)
from wtforms.validators import InputRequired, Optional, URL


class NewPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField(
        "Photo URL", validators=[Optional(), URL(message="Must be a valid URL")]
    )
    age = IntegerField("Age", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = HiddenField("Available", default="True")

    def validate_age(form, field):
        if field.data is None:
            return
        if field.data < 0 or field.data > 30:
            raise ValidationError("Age must be between 0 and 30.")

    def validate_species(form, field):
        if field.data.lower() not in ["dog", "cat", "porcupine"]:
            raise ValidationError("Species must be dog, cat, or porcupine.")


class EditPetForm(FlaskForm):
    """Form for adding pets."""

    photo_url = StringField(
        "Photo URL", validators=[Optional(), URL(message="Must be a valid URL")]
    )
    age = IntegerField("Age", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?")

    def validate_age(form, field):
        if field.data is None:
            return
        if field.data < 0 or field.data > 30:
            raise ValidationError("Age must be between 0 and 30.")
