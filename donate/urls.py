from django.conf.urls import url
from .views import donate

urlpatterns = [
    url(r'^$', donate, name='donate'),
]