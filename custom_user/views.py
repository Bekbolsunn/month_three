from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserListView(ListView):
    template_name = 'user_list.html'
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.all()


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'user_register.html'
    # success_url = reverse_lazy('users')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home:users')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_redirect_url(self):
        return redirect('home:users')

    