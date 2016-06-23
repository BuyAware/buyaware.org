from django.shortcuts import render
from django.conf import settings
from .models import PostModel

def blog(request):

    post_set = PostModel.objects.all().order_by('pub_date')[:settings.POSTS_PER_PAGE]

    return render(request, 'blog/blog.html', {'posts': post_set})
