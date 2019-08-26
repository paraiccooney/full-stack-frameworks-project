from django.conf.urls import url, include
from accounts.views import logout, login, registration
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    # include is used to append all the url_reset urls
    url(r'^password-reset/', include(url_reset))
]