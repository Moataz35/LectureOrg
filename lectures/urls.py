from django.urls import path
from .views import *

urlpatterns = [
    path('courses/', CoursesListCreateView.as_view()),
    path('courses/<int:pk>/', CourseEditRetrieveView.as_view()),
    path('links/', LinkListCreateView.as_view()),
    path('links/<int:pk>/', LinkEditRetrieveView.as_view()),
]
