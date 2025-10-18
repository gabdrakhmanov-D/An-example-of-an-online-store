from django import forms


class ContactForm(forms.Form):
    user_name = forms.CharField(label="Имя", max_length=100)
    user_email = forms.EmailField(label="Электронная почта")
    user_text = forms.CharField(label="Сообщение", widget=forms.Textarea)
