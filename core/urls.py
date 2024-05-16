from django.urls import path
from .views import frontpage, signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
