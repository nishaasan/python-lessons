from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

# Configuration
class Config:
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

# Initialize Flask app and database
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Define Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Define Forms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Logic to validate user login
        return redirect(url_for('blog'))
    return render_template('login.html', title='Login', form=form)

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        
        # Create a new BlogPost object and add it to the database
        new_post = BlogPost(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        
        # Redirect to the blog page to display the newly added post
        return redirect(url_for('blog'))
    
    # Query all existing blog posts from the database
    posts = BlogPost.query.all()
    
    return render_template('blog.html', title='Blog', form=form, posts=posts)


# Running the application
if __name__ == '__main__':
    app.run(debug=True,port=1000)
