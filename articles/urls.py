from django.conf.urls import url
from .views import all_articles, full_article, write

urlpatterns = [
    url(r'^$', all_articles, name='index'),
    url(r'^(?P<pk>\d+)/$', full_article, name='full_article'),
    url(r'^write/', write, name='write')
]