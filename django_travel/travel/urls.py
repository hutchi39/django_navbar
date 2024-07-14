from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('company/', views.company, name='Company'),
    path('destinations/', views.destinations, name='Destinations'),
    path('destinations/asia/', views.asia, name='Asia'),
    path('destinations/southeastasia/', views.southeastasia, name='Southeast Asia'),
    path('destinations/southeastasia/brunei/', views.brunei, name='Brunei'),
    path('destinations/southeastasia/cambodia/', views.cambodia, name='Cambodia'),
    path('destinations/southeastasia/indonesia/', views.indonesia, name='Indonesia'),
    path('destinations/southeastasia/laos/', views.laos, name='Laos'),
    path('destinations/southeastasia/malaysia/', views.malaysia, name='Malaysia'),
    path('destinations/southeastasia/philippines/', views.philippines, name='Philippines'),
    path('destinations/southeastasia/singapore/', views.singapore, name='Singapore'),
    path('destinations/southeastasia/thailand/', views.thailand, name='Thailand'),
    path('destinations/southeastasia/vietnam/', views.vietnam, name='Vietnam'),

    path('destinations/southasia/', views.southasia, name='South Asia'),
    path('destinations/southasia/sri_lanka/', views.sri_lanka, name='Sri Lanka')
]
