from django.contrib import admin
from models import *

from django.contrib.admin.util import flatten_fieldsets

from django import forms
from forms import CriterionInRatingFormSet, CriterionForm


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

    # initial fields that appear in any case
    fields = ['name', 'img', 'description', 'date_added', 'brand', 'rating'] 
    
    # extra dynamically added fields that require manual saving
    criteria_to_save = []
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super(ProductAdmin, self).get_fieldsets(request, obj)
        
        # get_fieldsets is called multiple times so we have to make sure that
        # extra_fields to save does not contain multiple times the same field
        # name
        self.criteria_to_save = []
        
        # Check if this is an add or change form
        # if it's a change form, proceed to add the dynamic criteria fields
        if (obj != None):
            
            # get all criterions which have to be answered for the selected
            # rating given to the product
            related_criteria = obj.rating.criterion_set.all()
            
            # iterate over every criteria needed to define the rating
            for criterion in related_criteria:
               
                # define name of field
                field_name = "Criterion_%d" % criterion.id

                self.criteria_to_save.append({
                    'field':field_name, 
                    'obj':criterion,
                })

                # find out if the answer to the criterion already exists for this rating and this product
                existing_answer_set = CriterionAnswer.objects.filter(criterion=criterion).filter(product=obj)

                # update declared fields with the appropriate field 
                # given the criterion type
                #
                # Boolean field for Yes/No types
                # Integer field for xx and xy types
                if(existing_answer_set.exists()):
                    if(criterion.crit_type == 'YN'):
                        self.form.declared_fields.update(
                            {field_name:forms.BooleanField(required=False,
                                                           initial=existing_answer_set[0].answer_bool,
                                                       )}
                        )
                    elif(criterion.crit_type == 'XX'):
                        self.form.declared_fields.update(
                            {field_name:forms.IntegerField(required=False,
                                                           initial=existing_answer_set[0].answer_xx,
                                                       )}
                        )

                    elif(criterion.crit_type == 'YY'):
                        self.form.declared_fields.update(
                            {field_name:forms.IntegerField(required=False,
                                                           initial=existing_answer_set[0].answer_xy,
                                                       )}
                        )

                 # add fieldset to returned fieldset list
                fieldsets.append([field_name, {
                    'fields': (field_name,),
                    'description': criterion.question,
                }])
        
        else: 
           pass

        return fieldsets

    
    def save_model(self, request, obj, form, change):
        
        # save data related to the product
        obj.save()
        
        # save data related to the rating if their is any data to save
        if(self.criteria_to_save):
            
            # iterate over each criteria
            for criterion_to_save in self.criteria_to_save:
                
                # find out if the answer to the criterion already exists for this rating and this product
                existing_answer_set = CriterionAnswer.objects.filter(criterion=criterion_to_save['obj']).filter(product=obj)

                # if it does exist...
                if(existing_answer_set.exists()):

                    # get the first existing answer
                    existing_answer = existing_answer_set[0]
                    print("Answer to criterion %d already exists for %s" % (criterion_to_save['obj'].id, obj.name))
                    print("saving changes...")

                    # modify field according to criterion type
                    if(criterion_to_save['obj'].crit_type == 'YN'):
                        existing_answer.answer_bool = form.cleaned_data[criterion_to_save['field']]
                    elif(criterion_to_save['obj'].crit_type == 'XX'):
                        existing_answer.answer_xx = form.cleaned_data[criterion_to_save['field']]
                    elif(criterion_to_save['obj'].crit_type == 'XY'):
                        existing_answer.answer_xy = form.cleaned_data[criterion_to_save['field']]
                    existing_answer.save()

                    # save changes
                    print("answer saved.")

                # if it doesn't exist...
                else:
                    
                    print("No Answer in db to criterion %d for %s" % (criterion_to_save['obj'].id, obj.name))
                    print("saving answer...")

                    # create a new answer
                    answer = CriterionAnswer()
                    answer.criterion = criterion_to_save['obj']
                    answer.product = obj

                    # modify field according to criterion type
                    if(criterion_to_save['obj'].crit_type == 'YN'):
                        answer.answer_bool = form.cleaned_data[criterion_to_save['field']]
                    elif(criterion_to_save['obj'].crit_type == 'XX'):
                        answer.answer_xx = form.cleaned_data[criterion_to_save['field']]
                    elif(criterion_to_save['obj'].crit_type == 'XY'):
                        answer.answer_xy = form.cleaned_data[criterion_to_save['field']]
                    # save newly created answer
                    answer.save()
                    print("answer saved.")
                

class CriterionInRatingInline(admin.TabularInline):
    model = CriterionInRating
    formset = CriterionInRatingFormSet            

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
        fields = ['criterion', 'product']
        
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
#admin.site.register(CriterionInRating, CriterionInRatingAdmin)
admin.site.register(CriterionAnswer, CriterionAnswerAdmin)
admin.site.register(Category, CategoryAdmin)
