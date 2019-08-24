from django.conf.urls import url
from .views import all_articles, full_article

urlpatterns = [
    url(r'^$', all_articles, name='index'),
    url(r'^(?P<pk>\d+)/$', full_article, name='full_article'),
]