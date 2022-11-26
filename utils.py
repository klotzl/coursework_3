import json
import logging
from json import JSONDecodeError


# ФЙНКЦИИ ДЛЯ РАБОТЫ С ПОСТАМИ И КОММЕНТАМИ
def load_posts(filename):
    """Загружает джейсон файлы"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        logging.info('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'


def get_posts_all(filename):
    """Выводит все посты"""
    return load_posts(filename)


def get_posts_by_user(user_name, filename):
    """Выводит посты пользователя по его имени
    , если имя не существует выдавать ошибку"""
    # if user_name in get_posts_all(filename):
    post_for_user = []
    for post in load_posts(filename):
        if user_name.lower() in post['poster_name'].lower():
            post_for_user.append(post)
    if not post_for_user:
        raise ValueError(f'Пользователя с именем {user_name} не существует')

    return post_for_user


def search_for_posts(query, filename):
    """Выводит посты в тексте которых присутствует query"""
    posts_for_query = []
    for post in get_posts_all(filename):
        if query.lower() in post['content'].lower():
            posts_for_query.append(post)
    return posts_for_query


def get_post_by_pk(pk, filename):
    """Выводит пост по id"""
    for post in get_posts_all(filename):
        if post['pk'] == pk:
            return post


def get_comments_by_post_id(post_id, post_file, comment_file):
    """Возвращает комментарии определенного поста"""
    if not get_post_by_pk(post_id, post_file):
        raise ValueError(f'Либо этого поста нет либо же у него нет комментов')
    all_comments = []
    for comments in load_posts(comment_file):
        if post_id == comments['post_id']:
            all_comments.append(comments)
    return all_comments
