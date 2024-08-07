from django.contrib import admin
from .models import Category,Post,Reklama,YoutubeVideo
# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Reklama)
admin.site.register(YoutubeVideo)
