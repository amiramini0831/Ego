from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .Serializers import *
from rest_framework import generics
from django.db.models import Q
from django.conf import settings

# ===========================================================================================================
class SliderListAPIView(generics.ListAPIView):
    queryset = Slider.objects.filter(Q(is_active=True)).order_by('-register_date')[:8]
    serializer_class = SliderSerializer
        
# ===========================================================================================================
class BlogsListView(generics.ListAPIView):
    queryset = Blog.objects.filter(Q(is_active=True)).order_by('-register_date')[:16]
    serializer_class = BlogSerializer
# ----------------------------------------------------------------
class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.filter(Q(is_active=True))
    lookup_field = 'slug'
    serializer_class = BlogSerializer
    

# ===========================================================================================================
class EventsListView(generics.ListAPIView):
    queryset = Events.objects.filter(Q(is_active=True)).order_by('-register_date')[:16]
    serializer_class = EventsSerializer
# ----------------------------------------------------------------
class EventDetailView(generics.RetrieveAPIView):
    queryset = Events.objects.filter(Q(is_active=True))
    lookup_field = 'slug'
    serializer_class = EventsSerializer
    
# ===========================================================================================================
