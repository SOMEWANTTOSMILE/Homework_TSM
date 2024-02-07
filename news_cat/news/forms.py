from django.contrib.auth.forms import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=255)
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    confirm_password = forms.CharField(max_length=255)

    class Meta:
        field = ['email', 'username', 'password', 'confirm_password']
