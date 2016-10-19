from django import forms
from models import CriterionAnswer
from django.core.exceptions import ValidationError

# --------------------
# Custom admin forms
# --------------------


class CriterionInRatingFormSet(forms.models.BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(CriterionInRatingFormSet, self).__init__(*args, **kwargs)
        print(dir(self))

    def clean(self):
        super(CriterionInRatingFormSet, self).clean()

        # count sum of all weightings and raise a validation error if the sum
        # is not equal to 100
        total_percentage = 0

        for form in self.forms:
            if(form.cleaned_data and form.cleaned_data.get("DELETE") == False):
                total_percentage += form.cleaned_data.get("weight")

        if total_percentage != 100 and total_percentage != 0:
            raise ValidationError("Sum of weights must be equal to 100")

class CriterionAnswerFormSet(forms.BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(CriterionAnswerFormSet, self).__init__(*args, **kwargs)
        
        #self.queryset = CriterionAnswer.objects.filter()