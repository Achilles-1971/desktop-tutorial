from django import forms
class UserForm(forms.Form):
    file = forms.ImageField(label="Изображение")
    date = forms.DateField(label="Введите дату")
    time = forms.DateField(label="Введите время")
    time_delta = forms.DurationField(label="Введите промежуток времени")
    date_time = forms.SplitDateTimeField(label="Введите дату и время")
    num = forms.IntegerField(label="Введите целое число")
    num = forms.DecimalField(label="Введите десятичное число", decimal_places=2)
    ling = forms.ChoiceField(label="Выберите язык", choices=((1, "Английский"),(2, "Немецкий"),
    (3, "Французский")))
    city = forms.TypedMultipleChoiceField(label="Выберите город",empty_value=None,choices=((1, "Москва"),
    (2, "Воронеж"),(3, "Курск"),(4, "Томск")))
    country = forms.MultipleChoiceField(label="Выберите страны",choices=((1, "Англия"),(2, "Германия"),
    (3, "Испания"),(4, "Россия")))
