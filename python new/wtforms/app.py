from flask import Flask, render_template, redirect, url_for
from forms import StudentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdef'  # Change this to a secret key

# Dummy data to store student records
students = []

@app.route('/', methods=['GET', 'POST'])
def index():
    form = StudentForm()

    if form.validate_on_submit():
        student_data = {
            'name': form.name.data,
            'age': form.age.data,
            'grade': form.grade.data
        }
        students.append(student_data)

    return render_template('index.html', form=form, students=students)

if __name__ == '__main__':
    app.run(debug=True)
