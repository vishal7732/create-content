from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import string 
import random
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


User = get_user_model()

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', default=True)
    metatitle = models.CharField(max_length=100, blank=True, null=True)
    metadesc = models.CharField(max_length=250, blank=True, null=True)
    

    def __str__(self):
        return self.title

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    About = RichTextUploadingField(blank=True)
    profile_picture = models.ImageField(upload_to='images/')
    alt_profile = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False)
    image = models.ImageField(upload_to='images/', default=True)
    alt = models.CharField(max_length=50,blank=True)
    overview = RichTextUploadingField()
    metatitle = models.CharField(max_length=100, blank=True, null=True)
    metadesc = models.CharField(max_length=250, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #comment_count = models.IntegerField(default = 0)
    #view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    
    



    def __str__(self):
        return self.title

    

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 
  
def unique_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.title) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
      
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4)) 
              
        return unique_slug_generator(instance, new_slug = new_slug) 
    return slug 

def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 
  
pre_save.connect(pre_save_receiver, sender = Post) 


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50, blank=False, null=False)
    body = models.TextField()
    email = models.CharField(max_length=100, blank=False, null=False)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username