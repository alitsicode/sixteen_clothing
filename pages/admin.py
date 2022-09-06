from django.contrib import admin
from .models import product,likes,IpAddress,bookmarks
from django.contrib import messages
from jalali_date.admin import ModelAdminJalaliMixin
# Register your models here.

# class productcommentsinline(admin.TabularInline):
#     model=comment
#     fields=['comment_text','is_suggest','user']
@admin.register(product)
class ProductAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    # use that def to pass image in django admin panel in list display
    list_display=['title','owner','cover_tag','is_published','stock']
    list_filter=['owner','is_published','stock']
    search_fields=['title','description']
    ordering=['-date_time_create','owner','is_published','stock']
    # inlines=[
    #     productcommentsinline
    # ]
    actions = ['make_published','make_draft','make_stocke']

    @admin.action(description='published selected posts')
    def make_published(self,request, queryset):
        queryset.update(is_published='p')
        messages.success(request,'your post successfuly published')
    @admin.action(description='draft selected posts')
    def make_draft(self,request, queryset):
        queryset.update(is_published='d')
        messages.success(request,'your post successfuly draft')
    @admin.action(description='make stock selected')
    def make_stocke(self,request, queryset):
        queryset.update(stock='have')
        messages.success(request,'your post successfuly stock')
@admin.register(likes)
class likesAdmin(admin.ModelAdmin):
    list_display=['post','user']
    list_filter=['post','user']
    ordering=['post']

# @admin.register(comment)
# class commentAdmin(admin.ModelAdmin):
#     list_display=['post','user','is_suggest']
#     list_filter=['post','user','is_suggest']

    actions = ['make_suggest']
    @admin.action(description='suggest selected posts ')
    def make_suggest(self,request, queryset):
        queryset.update(is_suggest=True)
        messages.success(request,'your post successfuly suggest')

admin.site.register(IpAddress)
admin.site.register(bookmarks)