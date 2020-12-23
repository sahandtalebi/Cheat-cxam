from django import forms


class LoginForms(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'یوزر نیم را وارد کنید'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'پسورد را وارد کنید'})
    )