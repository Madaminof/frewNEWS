from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import HomeView, CategoriesView, DetailsView, PostView, youtube_videos,DetailView,LatestNewsDetails

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('category/', CategoriesView.as_view(), name='category'),
    path('details/', DetailsView.as_view(), name='details'),
    path('post/<int:pk>', PostView.as_view(), name='post'),


    path('api/videos/', youtube_videos, name='api_videos'),

    path('detail/<int:pk>',DetailView.as_view() , name='detail'),
    path('latestnew/<int:pk>', LatestNewsDetails.as_view(), name='latestnew'),


    path('search/', views.search, name='search'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)