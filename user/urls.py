from django.urls import path
from .views import user_registration, user_login, user_logout

urlpatterns = [
    path('register/', user_registration, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]
