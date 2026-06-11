from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('appointment/', views.appointment_page, name='appointment'),

    path('my-appointments/', views.my_appointments, name='table'),

    path('edit/<int:id>/', views.edit_appointment, name='edit'),
    path('delete/<int:id>/', views.delete_appointment, name='delete'),
    path('doctor/<int:id>/', views.doctor_detail, name='doctor_detail'),
]