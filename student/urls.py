from django.urls import path
from student.views import *

urlpatterns = [
    path('signup',SignupView.as_view(),name='signup'),
    path('studenthome',StudentHomeView.as_view(),name='shome'),
    path('course_details/<int:cid>',CourseDetailsView.as_view(),name="course_details"),
    path('addtocart/<int:cid>',AddToCartView.as_view(),name='addtocart'),
]
