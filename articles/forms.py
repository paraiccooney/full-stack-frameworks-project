from django import forms
from .models import Comment, Article


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment', 'article_key', 'comment_author')

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ('headline', 'author', 'content', 'tag', 'image')