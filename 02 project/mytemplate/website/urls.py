
from django.urls import path
from.import views

urlpatterns = [

    path('',views.homepageview.as_view(), name='home'),
    path('about/',views.aboutpageview.as_view(), name='about'),
    path('contact/',views.contactpageview.as_view(), name='contact'),
]
