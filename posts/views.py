from django.shortcuts import render
from .models import Post
from .forms import PostCreatForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreatForm(data=request.POST,files = request.FILES)
        if form.is_valid():
            new_item=form.save(commit=False)
            new_item.user = request.user
            new_item.save()

    else:
        form = PostCreatForm(data=request.GET)

    return render(request , 'posts/create.html',{'form':form})

        

