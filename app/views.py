from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category,Post

#Home
class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        a1 = get_object_or_404(Category, name='Jahon')
        detail1 = Post.objects.filter(category=a1).order_by('-created_at').first()
        a2 = get_object_or_404(Category, name='Jamiyat')
        detail2 = Post.objects.filter(category=a2).order_by('-created_at').first()
        a3 = get_object_or_404(Category, name='Sport')
        detail3 = Post.objects.filter(category=a3).order_by('-created_at').first()
        a4 = get_object_or_404(Category, name='Fan-Texnika')
        detail4 = Post.objects.filter(category=a4).order_by('-created_at').first()
        a5 = get_object_or_404(Category, name='Iqtisodiyot')
        detail5 = Post.objects.filter(category=a5).order_by('-created_at').first()

        context = {
            'categories': categories,
            'detail1': detail1,
            'detail2': detail2,
            'detail3': detail3,
            'detail4': detail4,
            'detail5': detail5,
        }
        return render(request, 'index.html', context=context)


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


