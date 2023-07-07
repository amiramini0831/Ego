from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   path('slider/', views.SliderListAPIView.as_view(), name="slider_list"),
   path('blogs/', views.BlogsListView.as_view(), name="blogs_list"),
   path('blogs/<slug:slug>/', views.BlogDetailView.as_view(), name="blogs_detail"),
   path('events/', views.EventsListView.as_view(), name="events_list"),
   path('events/<slug:slug>/', views.EventDetailView.as_view(), name="events_detail"),
]
