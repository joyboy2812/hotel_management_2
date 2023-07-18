from django.urls import path
from . import views

urlpatterns = [
    path('manage-hotel/', views.manageHotel, name="manage-hotel"),
    path('create-hotel/', views.createHotel, name="create-hotel"),
    path('update-hotel/<int:pk>/', views.updateHotel, name="update-hotel"),
    path('delete-hotel/<int:pk>/', views.deleteHotel, name="delete-hotel"),
]