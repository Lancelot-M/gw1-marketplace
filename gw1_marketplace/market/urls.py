"""Path file"""

from django.urls import path
from market import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.create_order, name="add_order"),
    path('category/', views.home, name="home"),
    path('category/<str:category_name>/', views.category, name="category"),
    path('category/<str:category_name>/<int:page_nb>', views.category, name="category"),
    path('item/<str:item_name>/<int:page_nb>', views.item, name="item"),

    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
]