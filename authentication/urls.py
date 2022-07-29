from django.urls import path
from .views import login_view
from authentication import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name='login'),
    path('logout', views.logout, name='logout'),
    path('user/profile', views.profile, name='profile'),
    path('user/edit_photo/<int:id>', views.editPhoto, name='photo'),
    path('user/liste-utilisateurs', views.userList, name='list'),
    path('user/ajout-utilisateur', views.addUser, name='addUser'),
    path('user/modification-profil/<int:id>', views.updateUser, name='update'),
    path('user/mot-de-passe', views.change_password, name='password'),
    path('user/del/<int:id>', views.del_user, name="del_user"),
]