from django.urls import path
from student.views import *

urlpatterns = [
    path('signup',SignupView.as_view(),name='signup'),
    path('studenthome',StudentHomeView.as_view(),name='shome')
]
