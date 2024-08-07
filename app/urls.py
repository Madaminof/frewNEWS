from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import HomeView, CategoriesView, DetailsView, PostView, YoutubeVideoView, api_videos,DetailView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('category/', CategoriesView.as_view(), name='category'),
    path('details/', DetailsView.as_view(), name='details'),
    path('post/<int:pk>', PostView.as_view(), name='post'),

    path('videos/', YoutubeVideoView.as_view(), name='video_list'),
    path('api/videos/', api_videos, name='api_videos'),

    path('detail/<int:pk>',DetailView.as_view() , name='detail'),

    path('search/', views.search, name='search'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)