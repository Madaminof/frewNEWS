from django.shortcuts import render
from django.views import View
from .models import Category,Post

#Home
class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories,

        }
        return render(request, 'index.html',context=context)


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        post = Post.objects.all()
        context = {
            'categories': categories,
            'post': post,
        }
        return render(request, 'base.html',context=context)





class PostView(View):
    def get(self, request, pk):
        post = Post.objects.filter(category=pk)
        return render(request, 'categori.html', {'post': post})


class DetailsView(View):
    def get(self, request):
        return render(request, 'categori.html')


