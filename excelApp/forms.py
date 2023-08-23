from django import forms


class Form(forms.Form):
    fullname = forms.CharField(label='ФИО', max_length=100)
    phone = forms.CharField(label='Номер телефона', max_length=20)
    description = forms.CharField(label='Краткое описание', widget=forms.Textarea)
    file = forms.FileField(label='Прикрепите файл', required=False)
