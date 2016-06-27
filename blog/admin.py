from django.contrib import admin
from django.contrib.auth.models import User
from .models import PostModel, Image
from django import forms
from tinymce.widgets import TinyMCE


class ImageAdmin(admin.ModelAdmin):
    model = Image
    exclude = ('post',)

class ImageInline(admin.TabularInline):
    model = Image.post.through

class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 85, 'rows': 20}))

    class Meta:
        model = PostModel
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    model = PostModel
    inlines = [ImageInline,]
    form = PostAdminForm

    # Limit author query-set to staff members
    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].queryset = User.objects.filter(is_staff=True)
        form.base_fields['author'].label_from_instance = lambda obj: "%s %s" % (obj.last_name, obj.first_name)
        return form
    
# register models
admin.site.register(Image, ImageAdmin)
admin.site.register(PostModel, PostAdmin)

