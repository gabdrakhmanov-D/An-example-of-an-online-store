from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserLoginForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user)
        return redirect('catalog:home')

    def send_welcome_email(self, user):
        subject = 'Благодарим за регистрацию!'
        message = f'Здравствуйте {user.first_name} {user.last_name}!\nВы зарегистрированы на нашем сайте.'
        from_email = EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail(subject, message, from_email, recipient_list)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('catalog:home')