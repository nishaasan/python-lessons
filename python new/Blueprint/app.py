# app.py
from flask import Flask,render_template
from auth.auth_bp import auth_bp
from blog.blog_bp import blog_bp

app = Flask(__name__)
app.secret_key = '123456'  # Change this to a secure secret key
app.config['UPLOAD_FOLDER'] = 'static'

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(blog_bp, url_prefix='/')

# Default route to render the home page
@app.route('/')
def default_route():
    return render_template('blog/home.html')

if __name__ == '__main__':
    app.run(debug=True,port=1000)
