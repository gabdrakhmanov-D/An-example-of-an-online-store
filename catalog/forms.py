from django import forms

from catalog.models import Product


class ContactForm(forms.Form):
    user_name = forms.CharField(label="Имя", max_length=100)
    user_email = forms.EmailField(label="Электронная почта")
    user_text = forms.CharField(label="Сообщение", widget=forms.Textarea)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',
                  'description',
                  'category',
                  'purchase_price',
                  'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field, field_object in self.fields.items():
            field_object.widget.attrs.update({'class': 'form-control'})

            if field == 'description':
                field_object.widget.attrs.update({
                    'cols': '5',
                    'rows': '5'
                })
            elif field == 'purchase_price':
                field_object.widget.attrs.update({'step': '500'})

        # self.fields['name'].widget.attrs.update({
        #     'class': 'form-control',
        #     'placeholder': f'Введите наименование товара'
        # })

