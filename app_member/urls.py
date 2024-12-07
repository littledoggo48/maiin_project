from django.urls import path
from . import views

app_name = 'app_member'

urlpatterns = [
    path('sign_up/', views.registration, name = 'sign_up'),
    path('sign_in/', views.login_view, name='sign_in')
]