from django.shortcuts import render

# Create your views here.
def all_articles(request):
    return render(request, "index.html")