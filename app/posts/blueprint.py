from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models import Post, Tag

from .forms import PostForm

from app import db

posts = Blueprint('posts', __name__, template_folder= 'templates')

@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if 'POST' == request.method:
        title = request.form.get('title', '')
        body = request.form.get('body', '')
        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('some error')
        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)

@posts.route('/')
def index():
    search = request.args.get('search')
    if search:
        posts = Post.query.filter(Post.title.contains(search) | Post.body.contains(search)).all()
    else:
        posts = Post.query.order_by(Post.created.desc())
    return render_template('posts/index.html', posts=posts)

@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_detail.html', post=post)

@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)