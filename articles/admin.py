from django.contrib import admin
from .models import Article, Comment

# we're allowing our Post model to be accessable from
# the admin backend
admin.site.register(Article)
admin.site.register(Comment)