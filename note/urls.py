from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createnote', views.create_note, name="journal"),
    path('update/<str:pk>', views.edit_note, name="update"),
    path('delete/<str:pk>', views.delete_note, name = 'delete'),
    path('read/<str:pk>', views.read_note, name="read"),

]
