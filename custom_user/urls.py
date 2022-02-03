from django.urls import path
from . import views

app_name= 'home'
urlpatterns = [
    path('register/', views.RegisterUser.as_view()),
    path('users/', views.UserListView.as_view(),name='users'),
    path('login/', views.LoginUser.as_view(),name='login'),
]