from django.contrib.auth.forms import UserCreationForm

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
