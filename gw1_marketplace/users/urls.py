"""Path file"""

from django.urls import path
from users import views

urlpatterns = [
    path('test/', views.create_order),
]