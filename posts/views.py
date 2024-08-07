from django.shortcuts import render
from .models import Post
from .forms import PostCreatForm

# Create your views here.

def post_create(request):
    if request.method=='POST':
        from=PostCreatForm(data = request.POST)
        

