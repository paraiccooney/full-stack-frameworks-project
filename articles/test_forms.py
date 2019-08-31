from django.test import TestCase
from .forms import CommentForm, ArticleForm

# Create your tests here.

class TestCommentForm(TestCase):

    def test_comment_needs_more_than_comment_field(self):
        form = CommentForm({'comment': 'Comment content'})
        self.assertFalse(form.is_valid())
        
    def test_an_empty_comment_is_invalid_and_prompt_is_given(self):
        form = CommentForm({'article_key': '1', 'comment_author': 'user'})
        self.assertFalse(form.is_valid())
        # checks to see if the error returned equals the string provided
        self.assertEqual(form.errors['comment'], [u'This field is required.'])
        
class TestArticleForm(TestCase):
    
    def test_comment_needs_more_than_headline_and_content(self):
        form = ArticleForm({'headline': 'Sample Headline', 'content': 'Article Content'})
        self.assertFalse(form.is_valid())
    
    def test_image_is_required_and_prompted(self):
        form = ArticleForm({'headline': 'Sample Headline', 'author': 'user', 'content': 'Article Content', 'tag': 'tags'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['image'], [u'This field is required.'])

        