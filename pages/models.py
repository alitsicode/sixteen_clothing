from django.db import models
from accounts.models import Customeuser
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from star_ratings.models import Rating
from django.utils.translation import gettext_lazy as _
# Create your models here.
class IpAddress(models.Model):
    ip_address=models.GenericIPAddressField(verbose_name='ip_address')

class product(models.Model):
    status=(
        ('d','draft'),
        ('p','published'),
        ('i','investigation'),
        ('b','back'),
    )
    stock=(
        ('empty','empty'),
        ('have','have'),
        ('in_order','in_order'),
    )
    title=models.CharField(max_length=50)
    description=models.TextField()
    price=models.DecimalField(max_digits=6 , decimal_places=2)
    owner=models.ForeignKey(Customeuser,on_delete=models.CASCADE)
    cover=models.ImageField(upload_to='cover')
    is_published=models.CharField(max_length=1,choices=status,default='d')
    stock=models.CharField(max_length=8,choices=stock,default='have')
    hits=models.ManyToManyField(IpAddress,blank=True,through='hitsfilter',related_name='hits')
    date_time_create=models.DateTimeField(auto_now_add=True)
    date_time_edit=models.DateTimeField(auto_now=True)
    comments = GenericRelation(Comment)
    ratings = GenericRelation(Rating, related_query_name='products')
    class Meta:
        verbose_name='product'
    def __str__(self):
        return self.title

    # this def write to we can have image in django admin panel
    def cover_tag(self):
        return format_html('<img width=150px height=150px src="{}" />'. format(self.cover.url))
    

class likes(models.Model):
    user=models.ForeignKey(Customeuser,on_delete=models.CASCADE,related_name='likes')
    post=models.ForeignKey(product,on_delete=models.CASCADE,related_name='likes')
    def __str__(self):
        return f'{self.user.username} -- {self.post} '
    class Meta:
        verbose_name='likes'

class bookmarks(models.Model):
    user=models.ForeignKey(Customeuser,on_delete=models.CASCADE,related_name='bookmark')
    post=models.ForeignKey(product,on_delete=models.CASCADE,related_name='bookmark')
    def __str__(self):
        return f'{self.user.username} -- {self.post} '
    class Meta:
        verbose_name='bookmark'

class hitsfilter(models.Model):
    product=models.ForeignKey(product, verbose_name=_("product"), on_delete=models.CASCADE)
    ip_address=models.ForeignKey(IpAddress, verbose_name=_("ip_address"), on_delete=models.CASCADE)
    timecreated=models.DateTimeField(auto_now_add=True)

# class comment(models.Model):
#     comment_text=models.TextField(verbose_name=_('your Opinion:'))
#     is_suggest=models.BooleanField(default=True,verbose_name=_('suggest it?'))
#     user=models.ForeignKey(Customeuser,on_delete=models.CASCADE,related_name='comment')
#     post=models.ForeignKey(product,on_delete=models.CASCADE,related_name='comment')
#     date_time_created=models.DateTimeField(auto_now_add=True)
#     parent=models.ForeignKey('self',on_delete=models.CASCADE,related_name='replies',blank=True,null=True)
#     def __str__(self):
#         return f' for : {self.post.title} from : {self.user.username} '
#     class Meta:
#         verbose_name='comment'
