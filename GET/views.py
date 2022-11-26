from flask import render_template, Blueprint, request
from json import JSONDecodeError

from constants import POST_JSON, COMMENTS_JSON
from utils import *

get_blueprint = Blueprint('get_blueprint', __name__, template_folder='templates')

file_posts = 'data/comments.json'
file_comments = 'data/comments.json'
file_bookmarks = 'data/bookmarks.json'


@get_blueprint.route('/')
def posts_all():
    """Главная страница со всеми постами"""
    posts = get_posts_all(POST_JSON)
    return render_template('index.html', posts=posts)


@get_blueprint.route('/posts/<int:post_id>')
def comments_by_id(post_id):
    """Страница с постом по его pk"""
    post = get_post_by_pk(post_id, POST_JSON)
    comments = get_comments_by_post_id(post_id, POST_JSON, COMMENTS_JSON)
    cnt_comments = len(comments)
    return render_template('post.html', comments=comments, cnt_comments=cnt_comments, post=post)


@get_blueprint.route('/search')
def search_posts_for_query():
    """Страница с постами содержашими в тексте слово S"""
    query = request.args.get("s")
    posts = search_for_posts(query, POST_JSON)
    cnt_posts = len(posts)
    return render_template('search.html', posts=posts, cnt_posts=cnt_posts)


@get_blueprint.route('/users/<username>')
def posts_for_user(username):
    """Страница с постами пользователя по имени"""
    users_posts = get_posts_by_user(username, POST_JSON)
    return render_template('user-feed.html', posts=users_posts, username=username)



