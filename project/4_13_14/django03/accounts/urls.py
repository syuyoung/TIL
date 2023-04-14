from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update, name='update'),
    path('profile/delete/', views.delete, name='delete'),
    path('profile/password/', views.password_change, name='password_change'),
]
