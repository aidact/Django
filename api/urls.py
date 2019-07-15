from api import views
from django.urls import path

urlpatterns = [
    path('reviews/', views.ReviewListCreate.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view()),
    path('login/', views.login)
]