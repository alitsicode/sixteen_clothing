from django.urls import path
from . import views

urlpatterns = [
   path('contactus',views.contactus.as_view(),name='contactus'),
   path('aboutus',views.aboutus,name='aboutus'),
]