from flask import Blueprint, jsonify
from json import JSONDecodeError

from constants import POST_JSON
from utils import *
import logging

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='api_log.log')


@api_blueprint.route('/api/posts/')
def posts_all_api():
    """Выводит json всех постов"""
    logging.warning("Запрос /api/posts")
    posts = get_posts_all(POST_JSON)
    return jsonify(posts), 200


@api_blueprint.route('/api/posts/<int:pk>')
def post_by_pk(pk):
    """Выводит json поста по id"""
    post = get_post_by_pk(pk, POST_JSON)
    logging.warning(f"Запрос /api/posts/{pk}")
    return jsonify(post), 200
