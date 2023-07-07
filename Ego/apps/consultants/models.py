from django.db import models
from utils import FileUpload
from django.utils import timezone
# ======================================================================================================
class ColleagueType(models.Model):
    colleague_type = models.CharField(max_length=50,verbose_name="نوع همکار")
    
    def __str__(self):
        return f"{self.colleague_type}"
    
    class Meta:
        verbose_name = "همکار"
        verbose_name_plural = 'همکاران'
# ======================================================================================================
class ServiceType(models.Model):
    service_type = models.CharField(max_length=50, verbose_name="نوع خدمت")
    
    def __str__(self):
        return f"{self.service_type}"
    
    class Meta:
        verbose_name = "نوع خدمت"
        verbose_name_plural = 'انواع خدمات'
# ======================================================================================================
class ServicesCategori(models.Model):
    category = models.CharField(max_length=100, verbose_name="دسته بندی نوع خدمت")
    
    def __str__(self):
        return f"{self.category}"
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = 'دسته بندی ها'
# ======================================================================================================
class Services(models.Model):
    type_of_service = models.CharField(max_length=300, verbose_name="موضوع جلسه")
    client = models.CharField(max_length=100, verbose_name="کاربران مدنظر خدمت")
    time = models.CharField(max_length=50, verbose_name="مدت زمان خدمت")
    category = models.ForeignKey(ServicesCategori, verbose_name="دسته بندی خدمت", on_delete=models.CASCADE, related_name='service_subject')
    
    def __str__(self):
        return f"{self.client}-{self.type_of_service}"
    
    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = 'خدمات'
# ======================================================================================================
class Consultant(models.Model):
    name = models.CharField(max_length=50,verbose_name="نام")
    family = models.CharField(max_length=50,verbose_name="نام خانوادگی")
    birth_date =models.DateField(verbose_name="تاریخ تولد")
    education = models.CharField(max_length=150,verbose_name="تحصیلات",default="کارشناسی ارشد")
    expertise = models.CharField(max_length=400, verbose_name="تخصص",default="روانشناس")
    university = models.CharField(max_length=200, verbose_name="دانشگاه",default="دانشگاه تهران")
    language = models.CharField(max_length=50, verbose_name="زبان", default="انگلیسی-فارسی")
    description = models.TextField(verbose_name="توضیحات دکتر درباره اتاق درمان")
    medical_system_number = models.PositiveIntegerField(verbose_name="شماره نظام پزشکی")
    resume = models.TextField(verbose_name="رزومه")
    records_of_psychotherapy_services = models.TextField(verbose_name="سوابق خدمات روان درمانی")
    educational_and_research_records = models.TextField(verbose_name="سوابق آموزشی و پژوهشی")
    approach_and_specialized_field = models.TextField(verbose_name="رویکرد و زمینه تخصصی")
    educational_records = models.TextField(verbose_name="سوابق و مدارک تحصیلی")
    address = models.TextField(verbose_name="آدرس")
    id_code = models.IntegerField(verbose_name="شماره ملی و یا شماره پاسپورت")
    country = models.CharField(max_length=120, verbose_name="کشور محل سکونت")
    colleague_type = models.ForeignKey(ColleagueType, verbose_name="نوع همکار", on_delete=models.CASCADE, related_name='work_type')
    service_type = models.ForeignKey(ServiceType, verbose_name="نوع خدمت", on_delete=models.CASCADE, related_name='consultant_service')
    services = models.ForeignKey(Services, verbose_name="خدمات تخصصی پزشک", on_delete=models.CASCADE, related_name='doctor')
    
    def __str__(self):
        return f"{self.name}-{self.family}"
    
    class Meta:
        verbose_name = "پزشک"
        verbose_name_plural = 'پزشکان'

# ======================================================================================================

class ServicesDescription(models.Model):
    service_name = models.CharField(max_length=100, verbose_name="نام خدمت")
    service_client = models.CharField(max_length=50, verbose_name="کاربران دریافت کننده خدمت")
    description = models.TextField(verbose_name="توضیحات خدمت")
    file_upload = FileUpload('images','Services')
    image = models.ImageField(upload_to=file_upload.upload_to, verbose_name="تصویر خدمت")
    
    def __str__(self):
        return f"{self.service_name}-{self.service_client}"
    
    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = 'خدمات'
