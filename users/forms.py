from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",
                  "username",
                  "first_name",
                  "last_name",
                  "phone_number",
                  "avatar",
                  "country",
                  "password1",
                  "password2")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field, field_object in self.fields.items():
            field_object.widget.attrs.update({'class': 'form-control'})

            if field == "username":
                field_object.label = 'Логин'
                field_object.help_text = ''
                field_object.widget.attrs.update({'placeholder': 'Введите ваш логин'})

            if field == "country":
                field_object.label = "Страна"

            if field == "email":
                field_object.label = "Электронная почта"
                field_object.help_text = ''
                field_object.widget.attrs.update({'placeholder': 'Введите ваш email'})

            if field == "first_name":
                field_object.label = "Имя"
                field_object.help_text = ''
                field_object.widget.attrs.update({'placeholder': 'Введите ваше имя'})

            if field == "last_name":
                field_object.label = "Фамилия"
                field_object.help_text = ''
                field_object.widget.attrs.update({'placeholder': 'Введите вашу фамилию'})

            if field == "phone_number":
                field_object.label = "Номер телефона"
                field_object.help_text = ''
                field_object.widget.attrs.update({'placeholder': 'Введите номер телефона'})

            if field == "password1":
                field_object.label = "Пароль"
                field_object.help_text = ''
                field_object.widget.attrs.update({'placeholder': 'Придумайте пароль'})

            if field == "password2":
                field_object.label = "Повторите пароль"
                field_object.help_text = ''



