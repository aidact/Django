from django.urls import path
from api import views


urlpatterns = [
    path('reviews/', views.review_list),
    path('reviews/<int:pk>/', views.review_detail),

]