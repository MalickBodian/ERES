from django.urls import path
from .views import login_view
from authentication import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('edit_photo/<int:id>', views.editPhoto, name='photo'),
]