from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .models import Comment
from .forms import CommentForm
from django.conf import settings
from django.contrib.auth.models import User, Group
from django import template


"""register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() """

"""def is_member(user):"""
journalist=True
"""if user.groups.filter(name='journalists').exists():
        journalist= True
    else:
        journalist= False"""

# Create your views here.
def all_articles(request):
    articles = Article.objects.all().order_by('-published_date')
    media_path = settings.MEDIAFILES_LOCATION
    return render(request, "index.html", {"articles": articles, "media_path": media_path})
    
def full_article(request, pk):
    """
    render an individual article with comment section
    """
    article = get_object_or_404(Article, pk=pk) if pk else None
    comments = Comment.objects.filter(article_key=pk)
    
    """if the user is logged in get their details, if not return an empty string.
    This solves a bug when rendering create-comment functionality based on logged in status"""
    if request.user.is_authenticated:
        user = User.objects.get(email=request.user.email)
    else:
        user = ''
        
    # comment form submission
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            comment_form= CommentForm(request.POST)
            comment_form.save()
            return render(request, "fullarticle.html", {'article': article, 'comment_form': comment_form, 'comments': comments})
    
    # "normal" page request (view the article)
    else:
        article = get_object_or_404(Article, pk=pk)
        article.views += 1
        article.save()
        
        comment_form = CommentForm(initial={'article_key': pk, 'comment_author': user })
        
        return render(request, "fullarticle.html", {'article': article, 'comment_form': comment_form, 'comments': comments})
    
    
    
    
 