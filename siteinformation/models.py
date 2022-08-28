from django.db import models
from accounts.models import Customeuser
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
# Create your models here.
class contactmessage(models.Model):
    subject=models.CharField(max_length=100,verbose_name=_('subject'))
    body=models.TextField(verbose_name=_('your text'))
    author=models.ForeignKey(Customeuser,on_delete=models.CASCADE,verbose_name=_('author'))
    date_time_created=models.DateTimeField(auto_now_add=True,verbose_name=_('date_time_create'))
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name=_('contactmessage')

class aboutus_information(models.Model):
    title=models.CharField(max_length=200,verbose_name=_('title'))
    work_description=models.TextField(verbose_name=_('work_description'))
    work_image=models.ImageField(upload_to='work_image',verbose_name=_('work_image'))
    def __str__(self):
        return self.title
    def work_image_tag(self):
        return format_html('<img width=150px height=150px src="{}" />'. format(self.work_image.url))
    class Meta:
        verbose_name=_('aboutus_information')

