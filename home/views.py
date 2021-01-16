from django.shortcuts import render, get_object_or_404
from post.models import Post, Category
import datetime

# Create your views here.
def index(request):
    week_ago = datetime.date.today() - datetime.timedelta(days=1000)
    trends = Post.objects.filter(timestamp__gte = week_ago).order_by('-views')
    queryset = Post.objects.filter(featured=True)
    blog = Category.objects.all()
    recent_post = Post.objects.order_by('-timestamp')[:6]
    post1 = Post.objects.all()
    context = {
        'object_list': queryset, 'post': blog, 'recent_post':recent_post, 'post1':post1, 'trends':trends, 'blog':post1,
    }
    return render(request, "index.html", context)

def category(request):
    return render(request, "category.html")

def category_list(request, cats):
    category_post = Post.objects.filter(Category=cats)
    blog = Post.objects.all()
    recent_post = Post.objects.order_by('-timestamp')[:5]


    return render(request, "category_list.html", {'cats':cats, 'category_post':category_post, 'post':blog, 'recent_post':recent_post})


def search(request):
    query = request.GET["search_input"]
    allpost = Post.objects.filter(title__icontains=query)
    params = {'allpost':allpost, 'query':query}
    return render(request, "search.html", params)


def about(request):
    return render(request, "about.html")

def elements(request):
    return render(request, "elements.html")

def single_blog(request):
    return render(request, "single-blog.html")

def contact(request):
    return render(request, "contact.html")

def error_404_view(request, exception):
    return render(request,'404.html')

def comment(request):
    if request.method == "POST":
        user_name = request.POST['name']
        email = request.POST['email']
        body = request.POST['comment']
        
    return render(request, "index.html")