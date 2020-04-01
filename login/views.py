from .forms import AuthUserForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class MyprojectLoginView(LoginView):
    template_name = 'login/account_login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit-page')
    def get_success_url(self):
        return self.success_url