from django import forms


class QuestionForm(forms.Form):
    massage = forms.CharField(widget=forms.TextInput)

