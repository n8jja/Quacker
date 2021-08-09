from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('login/', LoginView.as_view(template_name='core/login.html'), name="login"),

]