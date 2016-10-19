from django.contrib import admin
from models import *

from django.contrib.admin.util import flatten_fieldsets

from django import forms
from forms import *

# --------------------
# Inlines
# --------------------


class CriterionAnswerInline(admin.TabularInline):
    model = CriterionAnswer

    # criterion answers can't be added, these are defined by the product
    # and selected rating
    def has_add_permission(self, request):
        return False


class GlobalProductRatingInline(admin.TabularInline):
    model = GlobalProductRating


# --------------------
# Model admins
# --------------------


class BrandAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    '''
    Admin class for Product model. 

    Adds necessary fieldsets to asses the product according to the assigned
    rating.
    '''

    inlines = [
        GlobalProductRatingInline,
        CriterionAnswerInline,
    ]

    # TODO: hide criterions that do not belong to the selected rating


class CriterionAdmin(admin.ModelAdmin):

    list_filter = ('category',)
    list_display = ('question', 'category', 'date_added', )


class CriterionAnswerAdmin(admin.ModelAdmin):
    '''
    Admin for Criterion Answer model.

    The form takes care of showing only the field that corresponds to 
    the related criterion's type.
    '''

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
            [field.name for field in obj._meta.fields]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# --------------------
# registration
# --------------------

admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Criterion, CriterionAdmin)
admin.site.register(CriterionAnswer, CriterionAnswerAdmin)
admin.site.register(GlobalProductRating)
