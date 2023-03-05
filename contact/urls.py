from . import views
from django.urls import include, path

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('inquiry', views.inquiry, name='inquiry'),

]
