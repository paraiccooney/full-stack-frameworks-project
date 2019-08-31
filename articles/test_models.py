from django.test import TestCase
from .models import Article, Comment
from django.utils import timezone


class TestArticleModel(TestCase):

    def test_views_default_to_zero(self):
        article = Article(headline="New Article")
        article.save()
        self.assertEqual(article.views , 0)
    
    def test_if_tag_contains_substring(self):
        article = Article(headline="Sample headline", tag="News, Russia, China")
        article.save()
        self.assertTrue("China" in article.tag)

class TestCommentModel(TestCase):
    
    def test_comment_submission(self):
        comment = Comment(comment="A sample comment", comment_author="User", article_key="4")
        comment.save()
        self.assertEqual(comment.comment, "A sample comment")
        self.assertEqual(comment.comment_author, "User")
        self.assertEqual(comment.article_key, "4")