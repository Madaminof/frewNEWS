from django.contrib import admin
from .models import Category,Post,Reklama,YoutubeVideo,LatestNews
# Register your models here.

admin.site.register(Post)
admin.site.register(Reklama)
admin.site.register(YoutubeVideo)
admin.site.register(LatestNews)
