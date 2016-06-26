from django.shortcuts import render
from django.conf import settings
from .models import PostModel, Image
from django.shortcuts import get_object_or_404


def blog_index(request):
    '''
    The main page of the blog. Shows the latest news.
    '''

    # get set of latest posts
    posts = PostModel.objects.all().order_by('pub_date')[:settings.POSTS_PER_PAGE]
    return render(request, 'blog/blog.html', {'posts': posts})


def post_detail(request, slug):
    '''
    post detail view.
    '''
    
    images = PostModel.objects.get(slug = slug).image_set.all()

    return render(request, 'blog/post_detail.html', {
        'post': get_object_or_404(PostModel, slug = slug),
        'images': images,
    })
