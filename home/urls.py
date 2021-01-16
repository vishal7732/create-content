
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.sitemaps.views import sitemap
from main.sitemap import BlogSitemap

sitemaps = {
    'posts':BlogSitemap()
}

urlpatterns = [
    path('', views.index, name="home"),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
    path('category', views.category, name="category"),
    path('comments', views.comment, name="comment"),
    path('search', views.search, name="search"),
    path('category/<str:cats>', views.category_list, name="category_list"),
    path('about', views.about, name="about"),
    path('elements', views.elements, name="elements"),
    path('single_blog', views.single_blog, name="single_blog"),
    path('contact', views.contact, name="contact"),
    

]
