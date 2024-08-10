from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Post,LatestNews
from django.db.models import Q
from django.http import JsonResponse
from .models import YoutubeVideo,VideoView


#Home
class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        posts = Post.objects.all()
        videos = VideoView.objects.all()
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

        b1 = get_object_or_404(Category, name='Jahon')
        latestnew1 = LatestNews.objects.filter(category=b1).order_by('-date').first()
        b2 = get_object_or_404(Category, name='Jamiyat')
        latestnew2 = LatestNews.objects.filter(category=b2).order_by('-date').first()
        b3 = get_object_or_404(Category, name='Sport')
        latestnew3 = LatestNews.objects.filter(category=b3).order_by('-date').first()
        b4 = get_object_or_404(Category, name='Fan-Texnika')
        latestnew4 = LatestNews.objects.filter(category=b4).order_by('-date').first()
        b5 = get_object_or_404(Category, name='Iqtisodiyot')
        latestnew5 = LatestNews.objects.filter(category=b5).order_by('-date').first()

        context = {
            'categories': categories,
            'posts': posts,
            'videos': videos,

            'detail1': detail1,
            'detail2': detail2,
            'detail3': detail3,
            'detail4': detail4,
            'detail5': detail5,

            'latestnew1':latestnew1,
            'latestnew2': latestnew2,
            'latestnew3': latestnew3,
            'latestnew4': latestnew4,
            'latestnew5': latestnew5,



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
        category = Category.objects.get(pk=pk)
        post = Post.objects.filter(category=pk).order_by('-created_at')

        return render(request, 'categori.html', {'post': post, 'category': category,'category_id': pk})


class DetailsView(View):
    def get(self, request):
        return render(request, 'categori.html')


class LatestNewsDetails(View):
    def get(self, request, pk):
        latest_news = LatestNews.objects.get(pk=pk)
        related_latest= LatestNews.objects.filter(category=latest_news.category_id).exclude(pk=pk)

        context = {
            'latest_news': latest_news,
            'related_latest':related_latest
        }
        return render(request, 'yangilik_detail.html',context=context)



class DetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        related_posts = Post.objects.filter(category=post.category_id).exclude(pk=pk)


        return render(request, 'details.html', {'post': post, 'related_posts': related_posts})



def youtube_videos(request):
    videos = YoutubeVideo.objects.all().values('name', 'link')
    return JsonResponse(list(videos), safe=False)





# Search
def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    return render(request, 'search_results.html', {'results': results, 'query': query})