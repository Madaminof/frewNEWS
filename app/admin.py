from django.contrib import admin
from .models import Post,Reklama,YoutubeVideo,LatestNews,VideoView
# Register your models here.

admin.site.register(Post)
admin.site.register(VideoView)
admin.site.register(Reklama)
admin.site.register(YoutubeVideo)
admin.site.register(LatestNews)
