# blog/blog_bp.py
from flask import Blueprint, render_template, session,redirect,url_for

blog_bp = Blueprint("blog", __name__, template_folder="templates")

# Assuming blog_posts is defined somewhere in this file or imported
blog_posts = [
       {
        "id": 1,
        "title": "Introduction to Flask",
        "content": """
            <p>Flask is a micro web framework for Python.</p>
           <img src="{{ url_for('static', filename='flask.png') }}" alt="Flask Image">

        """
    }
]
    


@blog_bp.route('/')
def home():
    user = session.get('user', None)
    return render_template('home.html', user=user, blog_posts=blog_posts)

@blog_bp.route("/post/<int:post_id>")
def view_post(post_id):
    user = session.get('user', None)
    if user and user['is_authenticated']:
        # Find the blog post with the given id
        post = next((post for post in blog_posts if post["id"] == post_id), None)

        if post:
            # Render the template with the specific blog post details and username
            return render_template("post.html", post=post, user=user)
        else:
            # Handle the case where the post with the given id is not found
            return "Post not found", 404
    else:
        # Redirect to login if the user is not authenticated
        return redirect(url_for('auth.login'))
