from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"


class Login_User(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = 'Вы залогинены'
    extra_context = {
        'title': 'Вход',
        'button_text': 'Войти'
        }

    def get_success_url(self):
        return reverse_lazy('home')


class Logout_User(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)