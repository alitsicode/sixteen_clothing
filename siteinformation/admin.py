from django.contrib import admin
from .models import contactmessage,aboutus_information
# Register your models here.
@admin.register(contactmessage)
class contactadmin(admin.ModelAdmin):
    list_display=['subject','author']
    list_filter=['subject','author']
    search_fields=['subject']
    ordering=['-date_time_created']

@admin.register(aboutus_information)
class aboutusadmin(admin.ModelAdmin):
    list_display=['title','work_image_tag']
    list_filter=['title']
    search_fields=['title']

