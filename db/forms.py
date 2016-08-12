from django import forms
from models import CriterionAnswer
from django.core.exceptions import ValidationError

# --------------------
# Custom admin forms
# --------------------

class CriterionInRatingFormSet(forms.models.BaseInlineFormSet):
    
     def clean(self):
        super(CriterionInRatingFormSet, self).clean()

        # count sum of all weightings and raise a validation error if the sum 
        # is not equal to 100
        total_percentage = 0

        for form in self.forms:
            if(form.cleaned_data and form.cleaned_data.get("DELETE") == False):
                total_percentage += form.cleaned_data.get("weight")
                
        if total_percentage != 100:
            raise ValidationError("Sum of weights must be equal to 100")
        
class CriterionForm(forms.ModelForm):

    def clean(self):
        super(CriterionForm, self).clean()

        print(dir(self))

        print(self.instance.crit_type)
        print(self.cleaned_data.get("best_grade"))
        print(self.cleaned_data.get("worst_grade"))

        if (self.instance.crit_type == 'YN' and (self.cleaned_data.get("best_grade") or self.cleaned_data.get("worst_grade"))):
            raise ValidationError("'best grade' and 'worst grade' fields must stay equal to 0 for 'YN' criterion types")
            

    # TODO: add javascript to show/hide best grade and worst grade fields
    # TODO: if criterion type is YN, save best grade and worst grade as 0.
