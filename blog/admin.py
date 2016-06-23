from django.contrib import admin
from django.contrib.auth.models import User
from .models import PostModel

class PostAdmin(admin.ModelAdmin):
    model = PostModel

    # Limit author query-set to staff members
    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].queryset = User.objects.filter(is_staff=True)
        form.base_fields['author'].label_from_instance = lambda obj: "%s %s" % (obj.last_name, obj.first_name)
        return form
    
# register models
admin.site.register(PostModel, PostAdmin)
