from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Issue
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from dal import autocomplete
from django.utils.html import format_html
from crispy_forms.layout import Field


class CreateIssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ['title', 'label', 'priority', 'type', 'component', 'description', 'assignee']
        # widgets = {
        #     'component': autocomplete.ModelSelect2Multiple(url='autocomplete',
        #         attrs={'data-html': True}),
        # }


    def __init__(self, *args, **kwargs):
        super(CreateIssueForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout('title', 'label', 'priority', 'type',
                                    Field('component', css_class="test"),
                                    'description', 'assignee','reporter','status',
                                    Submit('submit', 'Sign in')
                                    )