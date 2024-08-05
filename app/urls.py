from django.urls import path
from .views import HomeView,CategoriesView,AboutView,Contact,LatestNews
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('categori/', CategoriesView.as_view(), name='categori'),
    path('about/', AboutView.as_view(), name='about'),
    path('latest_news/', LatestNews.as_view(), name='latest_news'),
    path('contact/', Contact.as_view(), name='contact'),
    ]