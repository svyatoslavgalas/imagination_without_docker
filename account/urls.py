from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('edit/<int:image_id>/', views.image_edit, name='edit'),
    path('info/<int:image_id>/', views.image_info, name='info'),
]
