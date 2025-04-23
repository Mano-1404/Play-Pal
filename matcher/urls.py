from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.create_profile, name='create_profile'),
    path('add_sport/', views.add_sport, name='add_sport'),
    path('create_game/', views.create_game, name='create_game'),
    path('join/<int:game_id>/', views.join_game, name='join_game'),
    path('local_players/', views.view_local_players, name='view_local_players'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('view-players/', views.view_local_players, name='view_players'),
    path('my-profile/', views.my_profile, name='my_profile'),
]