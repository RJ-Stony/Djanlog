from django.shortcuts import render
from blog.models import Post

def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    context = {
        'recent_posts': recent_posts,
    }
    return render(request, 'pages/landing.html', context)

def about_me(request):
    return render(request, 'pages/about_me.html')
