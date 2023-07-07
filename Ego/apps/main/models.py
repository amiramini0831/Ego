from django.db import models
from utils import FileUpload
from django.utils import timezone
from django.utils.html import mark_safe
# ===================================================================================================
class Slider(models.Model):
    file_upload = FileUpload('images','Sliders')
    image = models.ImageField(upload_to=file_upload.upload_to, verbose_name="تصویر اسلاید")
    slide_name = models.CharField(max_length=50,verbose_name="عنوان اسلاید")
    title2 = models.CharField(max_length=50, null=True,blank=True, verbose_name="متن دوم")
    title3 = models.CharField(max_length=50, null=True,blank=True, verbose_name="متن سوم")
    link = models.URLField(max_length=50,null=True,blank=True, verbose_name="لینک")
    is_active = models.BooleanField(default=True, blank=True, verbose_name="وضعیت فعال/غیرفعال")
    register_date = models.DateTimeField(auto_now_add=False, verbose_name="تاریخ درج")
    publish_date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    update_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین بروز رسانی")
    slug = models.SlugField(max_length=50,verbose_name="لینک ادرس")
    
    def __str__(self):
        return f"{self.slide_name}"
    
    class Meta:
        verbose_name = "اسلاید"
        verbose_name_plural = 'اسلایدها'
        
    # def show_image_slide(self):
    #     return mark_safe(f'<img src="/media/{self.image}" style="width:80px;height:80px"/>')
    # show_image_slide.short_description = "تصویر اسلاید"
    
    # def link(self):
    #     return mark_safe(f'<a href="{self.slider_link}" target="_blank">link</a>')
    # link.short_description = "پیوندها"


# ===================================================================================================

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    family = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    birth_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="تاریخ تولد")
    code = models.IntegerField(verbose_name="کد نویسنده")
    file_upload = FileUpload('images','Authors')
    image = models.ImageField(upload_to=file_upload.upload_to, verbose_name="تصویر نویسنده")
    is_active = models.BooleanField(default=True, blank=True, verbose_name="وضعیت فعال/غیرفعال")
    slug = models.SlugField(max_length=80,verbose_name="لینک نویسنده")
    
    def __str__(self):
        return f"{self.name}-{self.family}"
    
    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = 'نویسندگان'

# ===================================================================================================

class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان مقاله")
    content = models.TextField(verbose_name="متن اصلی")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    reading_time = models.CharField(max_length=50, verbose_name="مدت زمان مظالعه")
    blog_field = models.CharField(max_length=50, verbose_name="حوزه مرتبط با مقاله")
    file_upload = FileUpload('images','Blog_Image')
    image = models.ImageField(upload_to=file_upload.upload_to, verbose_name="تصویر مقاله")
    is_active = models.BooleanField(default=True, blank=True, verbose_name="وضعیت فعال/غیرفعال")
    author = models.ForeignKey(Author , verbose_name="نویسنده مقاله" , on_delete=models.CASCADE, related_name='author_blogs')
    slug = models.SlugField(max_length=50,verbose_name="لینک مقاله")
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = 'مقالات'
    
    
# ===================================================================================================

class Status(models.Model):
    satus_title = models.CharField(verbose_name="وضعیت", max_length=100)
    
    def __str__(self):
        return f"{self.satus_title}"
    

# ===================================================================================================
class Events(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان رویداد")
    description = models.TextField(verbose_name="توضیحات رویداد")
    file_upload = FileUpload('images','Events')
    image = models.ImageField(upload_to=file_upload.upload_to, verbose_name="تصویر رویداد")
    register_date = models.DateTimeField(auto_now_add=False, verbose_name="تاریخ درج")
    start_date = models.DateTimeField(auto_now_add=False, verbose_name="تاریخ شروع")
    end_date = models.DateTimeField(auto_now=False, verbose_name="تاریخ پایان")
    duration = models.CharField(max_length=50, verbose_name="مدت زمان رویداد")
    location = models.TextField(verbose_name="محل برگزاری رویداد")
    organizer = models.CharField(max_length=50, verbose_name="برگزارکننده")
    price = models.PositiveIntegerField(verbose_name="هزینه ثبت نام")
    status = models.ForeignKey(Status, verbose_name="وضعیت", on_delete=models.CASCADE, related_name='events')
    is_active = models.BooleanField(default=True, blank=True, verbose_name="وضعیت فعال/غیرفعال")
    slug = models.SlugField(max_length=90,verbose_name="لینک رویداد")
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = 'رویدادها'

# ===================================================================================================
class EventsGallery(models.Model):
    event= models.ForeignKey(Events, verbose_name="رویداد", on_delete=models.CASCADE, related_name='event_pictures')
    file_upload = FileUpload('images','Event_Gallery')
    image_name = models.ImageField(upload_to=file_upload.upload_to, verbose_name="تصاویر رویداد")

    class Meta:
        verbose_name = 'گالری تصویر رویداد'
        verbose_name_plural = 'گالری تصاویر رویدادها'
# ===================================================================================================