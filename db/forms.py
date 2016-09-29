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


class CriterionForm(forms.ModelForm):

    def clean(self):
        super(CriterionForm, self).clean()

        if (self.instance.crit_type == 'YN' and (self.cleaned_data.get("best_grade") or self.cleaned_data.get("worst_grade"))):
            raise ValidationError("'best grade' and 'worst grade' fields must stay equal to 0 for 'YN' criterion types")

    # TODO: add javascript to show/hide best grade and worst grade fields

class CriterionAnswerFormSet(forms.BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(CriterionAnswerFormSet, self).__init__(*args, **kwargs)
        self.queryset = CriterionAnswer.objects.all()