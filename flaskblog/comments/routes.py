from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Comment, Post
from flaskblog.comments.forms import CommentForm
from flask import request

comments = Blueprint('comments', __name__)

@comments.route('/post/<int:post_id>/new_comment', methods=['GET', 'POST'])
@login_required
def new_comment(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            comment = Comment(content=form.content.data, article=post, author=current_user)
            db.session.add(comment)
            db.session.commit()
            flash('Your comment has been added to the post', 'success')
            #return redirect(url_for('posts.post', post_id=post.id))
            return redirect(url_for('comments.post_comments', post_id=post.id))
            #return redirect(url_for('posts.post', post_id=post.id, 'comments', comment_id=comment.id))
    return render_template('create_comment.html', title='Comment Post',
form=form, post_id=post_id)

@comments.route("/post/<int:post_id>/comment/<int:comment_id>")
def comment(post_id,comment_id):
    comment = Comment.query.get_or_404(comment_id)
    return render_template('comment.html', content=comment.content, comment=comment)

@comments.route("/post/<int:post_id>/comments")
def post_comments(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter(Comment.post_id == post_id).all()
    return render_template('comments.html', comments=comments, post_id=post_id)
