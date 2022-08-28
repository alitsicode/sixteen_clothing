from django.db import models
from accounts.models import Customeuser
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from star_ratings.models import Rating
from django.utils.translation import gettext_lazy as _
# Create your models here.
class IpAddress(models.Model):
    ip_address=models.GenericIPAddressField(verbose_name=_('ip_address'))

class product(models.Model):
    status=(
        ('d',_('draft')),
        ('p',_('published')),
        ('i',_('investigation')),
        ('b',_('back')),
    )
    stock=(
        ('empty',_('empty')),
        ('have',_('have')),
        ('in_order',_('in_order')),
    )
    title=models.CharField(max_length=50,verbose_name=_('title'))
    description=models.TextField(verbose_name=_('description'))
    price=models.DecimalField(max_digits=6 , decimal_places=2,verbose_name=_('price'))
    owner=models.ForeignKey(Customeuser,on_delete=models.CASCADE,verbose_name=_('author'))
    cover=models.ImageField(upload_to='cover',verbose_name=_('cover'))
    is_published=models.CharField(max_length=1,choices=status,default='d',verbose_name=_('is_pubished'))
    stock=models.CharField(max_length=8,choices=stock,default='have',verbose_name=_('stock'))
    hits=models.ManyToManyField(IpAddress,blank=True,through='hitsfilter',related_name='hits',verbose_name=_('views'))
    date_time_create=models.DateTimeField(auto_now_add=True,verbose_name=_('date_created'))
    date_time_edit=models.DateTimeField(auto_now=True,verbose_name=_('date_edited'))
    comments = GenericRelation(Comment,verbose_name=_('comments'))
    ratings = GenericRelation(Rating, related_query_name='products',verbose_name=_('rates'))
    class Meta:
        verbose_name=_('product')
    def __str__(self):
        return self.title

    # this def write to we can have image in django admin panel
    def cover_tag(self):
        return format_html('<img width=150px height=150px src="{}" />'. format(self.cover.url))
    

class likes(models.Model):
    user=models.ForeignKey(Customeuser,on_delete=models.CASCADE,related_name='likes',verbose_name=_('user'))
    post=models.ForeignKey(product,on_delete=models.CASCADE,related_name='likes',verbose_name=_('post'))
    def __str__(self):
        return f'{self.user.username} -- {self.post} '
    class Meta:
        verbose_name=_('likes')

class bookmarks(models.Model):
    user=models.ForeignKey(Customeuser,on_delete=models.CASCADE,related_name='bookmark',verbose_name=_('user'))
    post=models.ForeignKey(product,on_delete=models.CASCADE,related_name='bookmark',verbose_name=_('post'))
    def __str__(self):
        return f'{self.user.username} -- {self.post} '
    class Meta:
        verbose_name=_('bookmark')

class hitsfilter(models.Model):
    product=models.ForeignKey(product, verbose_name=_("product"), on_delete=models.CASCADE)
    ip_address=models.ForeignKey(IpAddress, verbose_name=_("ip_address"), on_delete=models.CASCADE)
    timecreated=models.DateTimeField(auto_now_add=True,verbose_name=_('timeview'))

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
