from django.shortcuts import render
from photologue.models import Gallery

# enables creation of image link-list for tinyMCE editor for blog
from tinymce.views import render_to_image_list


def image_link_list(request):
    '''
    return: image link_list
    Creates a link_list for the TinyMCE editor for the blog admin.
    '''
    print('Sending image links')
    
    blog_photos = Gallery.objects.get(title = 'blog').public()
    link_list = [(photo.title, photo.get_display_url()) for photo in blog_photos]
    return render_to_link_list(link_list)
