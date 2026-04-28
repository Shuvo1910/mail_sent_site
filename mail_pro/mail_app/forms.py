from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from mail_app.models import UserInfoModel, ContactModel 

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserInfoModel
        fields = [
            'username',
            'full_name',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            

class ContactForm(forms.ModelForm): 
    class Meta:
        model = ContactModel
        fields = [
            'subject',
            'email',
            'messages'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
