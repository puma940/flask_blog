from flask import render_template, request, Blueprint
from flaskblog.models import Post, all_posts

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    sorted_posts = Post.query.order_by(Post.date_posted.desc()).paginate(page, per_page=4)
    return render_template('home.html', sorted_posts=sorted_posts, all_posts=all_posts())

@main.route("/about")
def about():
    return render_template('about.html', title='About', all_posts=all_posts())
