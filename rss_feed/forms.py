from django import forms

class TextForm(forms.Form):
    text_search = forms.CharField(label='Text Search', max_length=100)