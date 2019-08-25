from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.models import User

# Create your views here.
def all_articles(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, "index.html", {"articles": articles})
    
def full_article(request, pk):
    """
    Create a view that returns a single
    Article object based on the article ID (pk) and
    render it to the 'full_article.html' template.
    Or return a 404 error if the post is
    not found
    """
    article = get_object_or_404(Article, pk=pk) if pk else None
    user = User.objects.get(email=request.user.email)
    
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            comment_form= CommentForm(request.POST)
            comment_form.save()
            return redirect(all_articles)
    
    else:
        article = get_object_or_404(Article, pk=pk)
        article.views += 1
        article.save()
        
        comment_form = CommentForm(initial={'article_key': pk, 'comment_author': user })
        
        comments = Comment.objects.filter(article_key=pk)
    
        return render(request, "fullarticle.html", {'article': article, 'comment_form': comment_form, 'comments': comments})
    
    
    
    
 