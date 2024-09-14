from django import forms
class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.IntegerField(min_value=1, max_value=120)
    weight = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)
    email = forms.EmailField(label="Электронный адрес")
    reklama = forms.BooleanField(label="Согласны получать рекламу")