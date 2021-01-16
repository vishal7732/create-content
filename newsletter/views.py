from django.shortcuts import render, redirect
from .models import newsletter
# Create your views here.

def newslet(request):
    if request.method == 'POST':
        emaol = request.POST['email']
        new_email = newsletter()
        new_email.email = emaol
        new_email.save()
        return redirect('/')
    return render(request, "blogs.html" , {'emaol':emaol})