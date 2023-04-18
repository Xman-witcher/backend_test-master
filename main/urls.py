from django.urls import path

from main import views

app_name = 'api'

urlpatterns = [
    path('', views.companies_view),
    path('employees/', views.employee_dropdown, name='employees'),
]
