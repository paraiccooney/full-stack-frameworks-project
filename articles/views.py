from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article
from .models import Comment
from .forms import CommentForm, ArticleForm
from django.conf import settings
from django.contrib.auth.models import User, Group
from django import template
from datetime import datetime, timedelta
from django.db.models import Count


# Create your views here.

# HOME PAGE WITH ALL ARTICLES
def all_articles(request):
    
    # check to see if user is a journalist
    user = request.user
    if user.groups.filter(name='journalists').exists():
        journalist= True
    else:
        journalist= False
    
    articles = Article.objects.all().order_by('-published_date')
    media_path = settings.MEDIAFILES_LOCATION
    return render(request, "index.html", {"articles": articles, "media_path": media_path, "journalist": journalist})
 

# INDIVIDUAL ARTICLE VIEW
def full_article(request, pk):
    """
    render an individual article with comment section
    """
    article = get_object_or_404(Article, pk=pk) if pk else None
    comments = Comment.objects.filter(article_key=pk)
    
    # check to see if user is a journalist
    user = request.user
    if user.groups.filter(name='journalists').exists():
        journalist= True
    else:
        journalist= False
    
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
            return render(request, "fullarticle.html", {'article': article, 'comment_form': comment_form, 'comments': comments, "journalist": journalist})
    
    # "normal" page request (view the article)
    else:
        article = get_object_or_404(Article, pk=pk)
        article.views += 1
        article.save()
        
        comment_form = CommentForm(initial={'article_key': pk, 'comment_author': user })
        
        return render(request, "fullarticle.html", {'article': article, 'comment_form': comment_form, 'comments': comments, "journalist": journalist})
    
    
# VIEW TO WRITE AN ARTICLE
def write(request, pk=None):

    """The if statement below ensures that if the user (or someone who is not logged in) has typed in the correct URL but they are not in the journalists user 
    group they will be redirected.  This is used to stop people breaking the intention of the code."""
    user = request.user
    if user.groups.filter(name='journalists').exists():
        journalist= True
        article = get_object_or_404(Article, pk=pk) if pk else None
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                article_form = form
                article_form.save()
                return(redirect(reverse('index')))
            
            
        
        else:
            new_article = ArticleForm(initial={'author': user})
            return render(request, "write.html", {"journalist": journalist, "new_article": new_article})
        
    else:
        return(redirect(reverse('index')))
        
        
# JOURNALIST DASHBOARD
def myDashboard(request):
    
    # check to see if user is a journalist
    user = request.user
    if user.groups.filter(name='journalists').exists():
        journalist= True
    else:
        journalist= False
    
    media_path = settings.MEDIAFILES_LOCATION
    
    pastWeek = datetime.today() - timedelta(days=7)
    articles = Article.objects.filter(author=user).order_by('-published_date')
    # this weeks articles
    last_week = published_date=datetime.now()-timedelta(days=7)
    twArticles = Article.objects.filter(author=user, published_date__gte=last_week).order_by('-published_date')
    
    # METRIC CALCULATIONS
    # THIS WEEK
    # calculating article count
    articleCount = articles.count()
    
    # calculating viewcount
    viewCount = 0
    for item in articles:
        viewCount += item.views
    
    # calculating comment count
    comments = Comment.objects.all()
    article_keys = []
    commentCount = 0
    
    for item in articles:
        article_keys.append(item.pk)
    
    author_article_keys = str(article_keys)
    
    commentArray = []
    
    for key in article_keys:
        
        for item in comments:
            string_key = str(key)
            if string_key in item.article_key:
                commentArray.append(item.article_key)
                commentCount += 1
    
    # THIS WEEK
    # calculating article count
    twArticleCount = twArticles.count()
    
    # calculating viewcount
    twViewCount = 0
    for item in twArticles:
        twViewCount += item.views
    
    # calculating comment count
    comments = Comment.objects.all()
    twArticle_keys = []
    twCommentCount = 0
    
    for item in twArticles:
        twArticle_keys.append(item.pk)
    
    author_article_keys = str(article_keys)
    
    twCommentArray = []
    
    for key in twArticle_keys:
        
        for item in comments:
            string_key = str(key)
            if string_key in item.article_key:
                twCommentArray.append(item.article_key)
                twCommentCount += 1
    
    return render(request, "dashboard.html", {"articles": articles, "media_path": media_path, "journalist": journalist, 
    "articleCount": articleCount, "viewcount": viewCount, 'user':user, 'comments': commentCount, 
    "twArticleCount": twArticleCount, "twViewcount": twViewCount, 'twComments': twCommentCount})
    

# EDIT ARTICLE
def editArticle(request, pk=None):
    
    # check to see if user is a journalist
    user = request.user
    if user.groups.filter(name='journalists').exists():
        journalist= True
    else:
        journalist= False
    
    article = get_object_or_404(Article, pk=pk) if pk else None
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(myDashboard)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'editarticle.html', {'edit_form': form, "journalist": journalist})