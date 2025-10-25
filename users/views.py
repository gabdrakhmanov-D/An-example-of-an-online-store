from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:home')

    # def form_valid(self, form):
    #     user = form.save()
    #     self.send_welcome_email(user.email, user.username, user.password)
    #     return super().form_valid(form)
    #
    # def send_welcome_email(self, user_email, login, password):
    #     subject = 'Добро пожаловать в нашу библиотеку!'
    #     message = f'Спасибо з а регистраицю! Ваш логин{login},\n Ваш пароль{password}'
    #     from_email = EMAIL_HOST_USER
    #     recipient_list = [user_email,]
    #     send_mail(subject, message, from_email, recipient_list)