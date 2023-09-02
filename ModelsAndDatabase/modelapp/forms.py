from django import forms


class Table1(forms.Form):
    name = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=True)
    desc = forms.TimeField(required=True)


