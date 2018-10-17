from flask import Blueprint
from flask import render_template
from flask import request

from models import Post, Tag

posts = Blueprint('posts', __name__, template_folder= 'templates')

@posts.route('/')
def index():
    search = request.args.get('search')
    if search:
        posts = Post.query.filter(Post.title.contains(search) | Post.body.contains(search)).all()
    else:
        posts = Post.query.all();
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