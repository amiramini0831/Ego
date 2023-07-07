from django.contrib import admin
from .models import *


# ==========================================================================================
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('slide_name','is_active','link','register_date',)
    list_filter = ('slide_name','is_active',)
    list_editable = ('is_active',)
    ordering =('register_date','is_active','slide_name',)
    search_fields =('slide_name','slider_title2','slider_title3',)
    # readonly_fields = ('show_image_slide',)
    
    
# ==========================================================================================
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','family','birth_date','is_active',)
    list_editable = ('is_active',)
    ordering =('name','family','is_active',)
    search_fields =('name','family',)
    
    
# ==========================================================================================
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','blog_field','is_active','author','register_date',)
    list_filter = ('blog_field','author',)
    list_editable = ('is_active',)
    ordering =('register_date','is_active','blog_field',)
    search_fields =('title','content',)


# ==========================================================================================
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('satus_title',)
    
    
# ==========================================================================================
class EventGalleryInlineAdmin(admin.TabularInline):
    model = EventsGallery
    extra = 3
# --------------------------------------------------
@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','price','is_active','location','status','register_date','start_date',)
    list_filter = ('title','is_active','status',)
    list_editable = ('is_active',)
    ordering =('register_date','is_active','status',)
    search_fields =('title','location',)
    inlines = [EventGalleryInlineAdmin]
    
# ==========================================================================================