from rest_framework import serializers
from .models import *

# ========================================================================================================

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ['register_date','is_active','publish_date','update_date']
        
# ========================================================================================================

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
# ========================================================================================================

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['is_active']
        
# ========================================================================================================

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
        
# ========================================================================================================

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        exclude = ['is_active']
        
# ========================================================================================================

