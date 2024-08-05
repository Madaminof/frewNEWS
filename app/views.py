from django.shortcuts import render
from django.views import View
from .models import Category,Post

# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class CategoriesView(View):
    def get(self, request):
        categori = Category.objects.all()
        post = Post.objects.all()
        context = {
            'categories': categori,
            'post': post,
        }
        return render(request, 'categori.html',context=context)


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')



class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')


class LatestNews(View):
    def get(self, request):
        return render(request, 'latest_news.html')

