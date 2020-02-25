from django.contrib import admin
from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .models import Component
urlpatterns = [
    path(
        'autocomplete/',
        views.Home.as_view(model= Component, create_field='component'),
        name='autocomplete',
    ),
    path('', views.home, name ="home"),
    path('user', views.user, name='user'),
    path('user/<username>', views.user, name='profile'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True),
         name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)