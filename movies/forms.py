from crispy_forms.helper import FormHelper
from django import forms


class MovieGETForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "GET"
        self.helper.form_action = "submit_form"
        self.helper.form_id = "id-getForm"

    title = forms.CharField(max_length=100)
    description = forms.TextField()
    year = forms.IntegerField()
    poster = forms.URLField()
    trailer = forms.URLField()
