from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    success_message = _("You are logged in")
    extra_context = {
        "title": _("Login"),
        "button_text": _("Enter"),
    }

    def get_success_url(self):
        return reverse_lazy("home")


class LogoutUser(LogoutView):
    next_page = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)