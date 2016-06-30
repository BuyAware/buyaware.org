from django.contrib import admin
from django.contrib.auth.models import User
from buyaware import settings

# Import extra models
from .models import PostModel
from photologue.models import Gallery

# Import form customisation classes
from django import forms
from tinymce.widgets import TinyMCE

# Import model translation classes to adapt admin to django-modeltranslation
from modeltranslation.admin import TranslationAdmin
from . import translation



class PostAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostAdminForm, self).__init__(*args, **kwargs)
        for lang_code in settings.LANGUAGES : 
            self.fields['body_'+lang_code[0]] = forms.CharField(widget=TinyMCE(attrs={'cols': 85, 'rows': 20}))

    class Meta:
        model = PostModel
        fields = '__all__'

class PostAdmin(TranslationAdmin):
    model = PostModel
    form = PostAdminForm

    def get_authors(self, obj):
        '''
        input:
        - user: django user model
        output:
        - string: author name
        Checks if the user has a first name and a last name defined.
        If the check is positive, these are returned. If negative, the username
        is returned. This method is used to populate the author selection list.
        '''
        if(obj.last_name and obj.first_name):
            return "%s %s" % (obj.last_name, obj.first_name)
        else:
            return "%s" % (obj.username)
        

    def get_form(self, request, obj=None, **kwargs):
        '''
        Overrides get_form from ModelAdmin.
        Limit author query-set to staff members
        '''
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].queryset = User.objects.filter(is_staff=True)
        form.base_fields['author'].label_from_instance = self.get_authors
        # form.base_fields['author'].label_from_instance = lambda obj: "%s %s" % (obj.last_name, obj.first_name)
        return form
    
# register models
admin.site.register(PostModel, PostAdmin)

