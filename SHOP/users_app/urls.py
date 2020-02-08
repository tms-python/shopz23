from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView



app_name = 'users_app'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('users_app:login')), name='logout'),
]
