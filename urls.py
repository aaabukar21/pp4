from django.urls import path
from booking import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_table, name='book'),
]
