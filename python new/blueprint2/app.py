from flask import Flask, render_template, Blueprint

app = Flask(__name__)

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/post')
def post_list():
    return render_template('post_list.html', title='Posts')

app.register_blueprint(posts_bp)

@app.route('/')
def home():
    return render_template('base.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True,port=2000)
