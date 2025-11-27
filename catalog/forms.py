from django import forms
from django.core.exceptions import ValidationError

from catalog.custom_validators import ForbiddenWordsValidator
from catalog.models import Product
from users.utils import UserSettingUpMix


class ContactForm(forms.Form):
    user_name = forms.CharField(label="Имя", max_length=100)
    user_email = forms.EmailField(label="Электронная почта")
    user_text = forms.CharField(label="Сообщение", widget=forms.Textarea)


class ProductForm(UserSettingUpMix,forms.ModelForm):
    MAX_UPLOAD_SIZE = 5 * 1024 ** 2
    ALLOWED_TYPES = ['image/jpeg', 'image/png']

    class Meta:
        model = Product
        fields = ['name',
                  'description',
                  'category',
                  'is_publish',
                  'purchase_price',
                  'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.validation = ForbiddenWordsValidator()

        for field, field_object in self.fields.items():

            if field == 'description':
                field_object.widget.attrs.update({
                    'cols': '5',
                    'rows': '5'
                })
            elif field == 'purchase_price':
                field_object.widget.attrs.update({'step': '500'})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validation(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validation(description)
        return description

    def clean_purchase_price(self):
        price = self.cleaned_data.get('purchase_price')
        if price <= 0:
            raise ValidationError('Цена должна быть больше 0')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            if image.content_type not in self.ALLOWED_TYPES:
                raise ValidationError('Недопустимый тип файла. Можно загрузить только файлы типов: .jpeg, .png.')

            elif image.size > self.MAX_UPLOAD_SIZE:
                raise ValidationError('Ваше изображение превышает допустимый лимит 5 МВ.')
        return image
