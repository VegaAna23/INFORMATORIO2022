from django.contrib import admin
from .models import Post
from .models import Autor


admin.site.register(Post)
admin.site.register(Autor)