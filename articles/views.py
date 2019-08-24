from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

# Create your views here.
def all_articles(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles})
    
def full_article(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    article = get_object_or_404(Article, pk=pk)
    article.views += 1
    article.save()
    return render(request, "fullarticle.html", {'article': article})