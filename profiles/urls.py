from django.urls import path
from profiles import views


urlpatterns = [
    path('', views.profile_view, name='profile'),
]