from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def blog(request):
    blog = Post.objects.all()
    paginator = Paginator(blog, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    recent_post = Post.objects.order_by('-timestamp')[:5]
    post = {
        'post': blog, 'posts':posts, 'paginator':paginator, 'recent_post':recent_post, 'blog':blog
    }
    return render(request, "blogs.html", post)

def blogs(request,slug): 
    blog1 = Post.objects.get(slug=slug)
    blog1.views = blog1.views + 1 
    blog1.save()
    recent_post = Post.objects.order_by('-timestamp')[:5]
    blog = Post.objects.all()
    post2= get_object_or_404(Post, slug=slug)

    post1 = {
        'blog1':blog1, 'posts':post2, 'recent_post':recent_post, 'blog':blog
    }
 
    return render(request, "post.html", post1)


