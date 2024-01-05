from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit
from django import forms

from ai.settings import ALLOWED_INPUT_FILE_CONTENT_TYPES


class InputForm(forms.Form):
    input_file = forms.FileField(label='Input text file')

    def clean_input_file(self):
        input_file = self.cleaned_data['input_file']
        if input_file.content_type not in ALLOWED_INPUT_FILE_CONTENT_TYPES:
            raise forms.ValidationError(f'Only {",".join(ALLOWED_INPUT_FILE_CONTENT_TYPES)} content types are allowed')
        return input_file

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = self.__class__.__name__.lower()

        self.helper.layout = Layout(
            Div(
                Field("input_file", css_class="form-control-lg"),
            ),
            Submit(
                "save_text",
                "Submit",
            ),

        )
