from django.urls import path
from api import views


# urlpatterns = [
#     path('reviews/', views.review_list),
#     path('reviews/<int:pk>/', views.review_detail),
#
# ]

urlpatterns = [
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view()),
    path('users/', views.UserList.as_view()),
]