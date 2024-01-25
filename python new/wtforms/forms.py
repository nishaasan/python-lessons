from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class StudentForm(FlaskForm):
    name = StringField('Name')
    age = IntegerField('Age')
    grade = StringField('Grade')
    submit = SubmitField('Submit')
