from django.shortcuts import render
from articles.models import Article

# Create your views here.
def do_search(request):
    # search functionality based on headline, article tags, or author name
    articles = Article.objects.filter(headline__icontains=request.GET['search']) | Article.objects.filter(tag__icontains=request.GET['search']) | Article.objects.filter(author__icontains=request.GET['search'])
    return render(request, "index.html", {"articles": articles})
    