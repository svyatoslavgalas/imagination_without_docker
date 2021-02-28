from django.urls import path

from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.upload_image, name='upload'),
]
