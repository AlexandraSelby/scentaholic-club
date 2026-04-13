from django import forms
from .models import WeeklyPoll


class VoteForm(forms.Form):
    fragrances = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Choose up to three fragrances"
    )

    def __init__(self, *args, poll=None, **kwargs):
        super().__init__(*args, **kwargs)
        if poll:
            self.fields["fragrances"].queryset = poll.fragrances.all()

    def clean_fragrances(self):
        fragrances = self.cleaned_data["fragrances"]
        if len(fragrances) > 3:
            raise forms.ValidationError("You can choose up to three fragrances only.")
        return fragrances