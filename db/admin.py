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
    formset = CriterionAnswerFormSet 

    # criterion answers can't be added, these are defined by the product
    # and selected rating
    def has_add_permission(self, request):
        return False


class CriterionInRatingInline(admin.TabularInline):
    model = CriterionInRating
    formset = CriterionInRatingFormSet


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



class RatingAdmin(admin.ModelAdmin):
    inlines = [
        CriterionInRatingInline,
    ]

    list_display = ['name', 'criteria_count', 'is_active', 'date_added', ]

    def criteria_count(self, obj):
        return str(CriterionInRating.objects.filter(rating=obj).count())


class CriterionAdmin(admin.ModelAdmin):
    form = CriterionForm

    list_filter = ('category',)
    list_display = ('question', 'category', 'date_added', )


class CriterionAnswerAdmin(admin.ModelAdmin):
    '''
    Admin for Criterion Answer model.

    The form takes care of showing only the field that corresponds to 
    the related criterion's type.
    '''

    readonly_fields = []

    def get_fields(self, request, obj=None):
        # get_fields is called multiple times so we have to make sure the
        # fields aren't added many times and that there are always the
        # following fields
        fields = ['criterion', 'product', 'rating']

        # the diyplay of the model instance depends on it's type...
        criterion_type = obj.criterion.crit_type

        if(criterion_type == 'YN'):
            fields.append("answer_bool")
        elif(criterion_type == 'XX'):
            fields.append('answer_xx')
        elif(criterion_type == 'XY'):
            fields.append('answer_xy')

        return fields

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
            [field.name for field in obj._meta.fields]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CategoryAdmin(admin.ModelAdmin):
    pass


# --------------------
# registration
# --------------------

admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Criterion, CriterionAdmin)
admin.site.register(CriterionAnswer, CriterionAnswerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GlobalProductRating)
