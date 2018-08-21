from django.contrib import admin
from .models import Post, Comment, Cidade, Eleitor

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Cidade)
admin.site.register(Eleitor)
