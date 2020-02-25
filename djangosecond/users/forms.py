from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True, max_length=255)
    last_name = forms.CharField(required=True, max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None
        self.fields['password2'].help_text = None
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0',
                       title="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
                Column('email', css_class='form-group col-md-6 mb-0', title='Your email'),
                css_class='form-row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0', title='Your name'),
                Column('last_name', css_class='form-group col-md-6 mb-0', title='Your last name'),
                css_class='form-row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0', title=
"Your password can’t be too similar to your other personal information.\n\
Your password must contain at least 8 characters.\n\
Your password can’t be a commonly used password.\n\
Your password can’t be entirely numeric."),
                Column('password2', css_class='form-group col-md-6 mb-0',
                       title="Enter the same password as before, for verification."),
                css_class='form-row'
            ),
            Submit('submit', 'Sign in')
        )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True, max_length=255)
    last_name = forms.CharField(required=True, max_length=255)

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['username'].help_text = None
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
        self.fields['image'].widget.attrs.update({'class': 'border-0 pl-0', 'style': "background:none"})
        self.helper.layout = Layout(
            Column('image', css_class='col-md-12 mb-0 p-0')
        )

    class Meta:
        model = Profile
        fields = ['image']
