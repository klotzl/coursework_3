#import pytest

from utils import posts_wish_teg

posts = [[{'content': 'Привет я тут делау #тест #функции на #pyton'}],
         [{'content': 'Привет я тут делау #тест #функции на #pyton', 'teg_words': ['тест', 'функции', 'pyton']}]]

print(posts_wish_teg([{'content': 'Привет я тут делау #тест #функции на #pyton'}]))

# @pytest.mark.parametrize("post, post_with_teg", posts)
# def test_posts_wish_teg(post, post_with_teg):
#     assert posts_wish_teg(post) == post_with_teg
