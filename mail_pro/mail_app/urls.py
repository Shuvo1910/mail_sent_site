from django.urls import path
from mail_app.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('contact/', contact_page, name='contact_page'),
]
