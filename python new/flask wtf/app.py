from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456' 

# Define a simple form using Flask-WTF and WTForms
class SimpleForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        # Process the form data (you can save it to a database or perform other actions)
        name = form.name.data
        return f'Thank you, {name}!'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True,port=1000)
