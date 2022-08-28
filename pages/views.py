from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from .models import product,likes,bookmarks
from .forms import profile_form
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
# Create your views here.
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from accounts.models import Customeuser
from django.core.paginator import Paginator
from .mixin import fieldmixin,authormixin,superusermixin
from django.db.models import Count,Q,Avg,Sum
from datetime import timedelta
from django.utils import timezone


def homeprouct(request):
    lastproduct=product.objects.filter(is_published = 'p').order_by('-date_time_create')[0:6]
    last_month=timezone.now() - timedelta(days=30)
    lastproduct=product.objects.filter(is_published = 'p').annotate(count=Count('hits',filter=Q(hitsfilter__timecreated__gt=last_month))).order_by('-count','-date_time_create')[:5]
    hot_product=product.objects.filter(is_published = 'p').annotate(count=Count('comments',filter=Q(comments__posted__gt=last_month) and Q(comments__content_type_id=7))).order_by('-count','-date_time_create')[:5]
    rated_product=product.objects.filter(is_published = 'p').annotate(count=Count('ratings',filter=Q(ratings__time_rated__gt=last_month) and Q(ratings__content_type_id=7))).order_by('-ratings__average',)[:5]
    return render(request,'pages/home.html',context={'lastproduct':lastproduct,'hot_product':hot_product,'rated_product':rated_product})

class listshop(generic.ListView):
    queryset=product.objects.filter(is_published = 'p')
    paginate_by=3
    template_name='pages/listproduct.html'
    context_object_name='allproduct'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_month=timezone.now() - timedelta(days=30)
        context["viewed_product"] =product.objects.filter(is_published = 'p').annotate(count=Count('hits',filter=Q(hitsfilter__timecreated__gt=last_month))).order_by('-count','-date_time_create')[:5]
        context["hot_product"] =product.objects.filter(is_published = 'p').annotate(count=Count('comments',filter=Q(comments__posted__gt=last_month))).order_by('-count','-date_time_create')[:5]
        context["rated_product"] =product.objects.filter(is_published = 'p').annotate(count=Count('ratings',filter=Q(ratings__time_rated__gt=last_month) and Q(ratings__content_type_id=7))).order_by('-ratings__average',)[:5]
        return context
    

@login_required
def detailshop(request,pk):
    detailproduct=get_object_or_404(product,pk=pk)
    if request.user.likes.filter(post=detailproduct,user=request.user).exists(): #related_name from user to find like or not
        is_liked=True
    else:
        is_liked=False
    
    if request.user.bookmark.filter(post=detailproduct,user=request.user).exists():
        besaved=True
    else:
        besaved=False
        
    ip_address=request.user.ip_address
    if ip_address not in detailproduct.hits.all():
        detailproduct.hits.add(ip_address)
    return render(request,'pages/detailproduct.html',context={'detailproduct':detailproduct,'is_liked':is_liked,'is_bookmark':besaved})

class createshop(LoginRequiredMixin,fieldmixin,generic.CreateView):
    model=product
    template_name='pages/createproduct.html'
    success_url='/admin_home'
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            instance=form.save(commit=False)
            instance.owner=self.request.user
            if not instance.is_published in ['d','i']:
                instance.is_published='d'
            instance.stock='in_order'
            instance.save()
        messages.success(self.request, _("your product successfuly add"))
        return super().form_valid(form)



class updateshop(fieldmixin,authormixin,SuccessMessageMixin,generic.UpdateView):
    model=product
    template_name='pages/updateproduct.html'
    success_url='/admin_home'
    context_object_name='products'
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            instance=form.save(commit=False)
            instance.owner=self.request.user
            if not instance.is_published in ['d','i']:
                instance.is_published='d'
            instance.stock='in_order'
            instance.save()
        messages.info(self.request, _("your product successfuly update"))
        return super().form_valid(form)

class deleteshop(superusermixin,generic.DeleteView):
    model=product
    template_name='pages/deleteproduct.html'
    success_url='/admin_home'
    context_object_name='product'
    # success_message='your product successfuly deleted ):'
    def form_valid(self, form):
        messages.error(self.request, _("your product successfuly deleted"))
        return super().form_valid(form)

def like(request,pk):
    mypost=get_object_or_404(product,pk=pk)
    try:
        like=likes.objects.get(post=mypost,user=request.user)
        like.delete()
        return JsonResponse({"response":"unliked"})

    except:
        likes.objects.create(post=mypost , user=request.user)
        return JsonResponse({"response":"liked"})

def save_post(request,pk):
    mypost=get_object_or_404(product,pk=pk)
    try:
        save=bookmarks.objects.get(post=mypost,user=request.user)
        save.delete()
    
    except:
        bookmarks.objects.create(post=mypost , user=request.user)
    return redirect('detailproduct',pk)


class search(generic.ListView):
    template_name = "pages/search_product.html"
    paginate_by=3
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = product.objects.filter(is_published='p').filter(Q(title__icontains=query) | Q(description__icontains=query))
        return object_list
class filter_product(generic.ListView):
    template_name = "pages/filter_product.html"
    paginate_by=6
    def get_queryset(self):  # new
        query = self.request.GET.get("f")
        object_list = product.objects.filter(is_published='p').order_by('-date_time_create').filter(Q(stock__exact=query))
        return object_list
class filter_by_price(generic.ListView):
    template_name = "pages/filter_product.html"
    paginate_by=6
    def get_queryset(self):  # new
        query = self.request.GET.get("vol")
        object_list = product.objects.filter(is_published='p').order_by('-date_time_create').filter(Q(price__range=(0,query)))
        return object_list

class saved(LoginRequiredMixin,generic.ListView):
    model=bookmarks
    template_name='pages/bookmarks.html'
    context_object_name='bookmark'
    paginate_by=3
    
@login_required
def user_each_post(request,pk):
    my_user=get_object_or_404(Customeuser,pk=pk)
    user_post=product.objects.filter(owner=my_user)
    paginator = Paginator(user_post , 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'pages/user_each_post.html',context={'user_posts':page_obj})


class admin_product_list(generic.ListView):
    template_name='pages/admin_home.html'
    context_object_name='admin_list_product'
    paginate_by=10
    def get_queryset(self):
        if self.request.user.is_superuser:
            return product.objects.all().order_by('-date_time_create','-ratings','-hits')
        elif self.request.user.is_author:
            return product.objects.filter(owner=self.request.user).order_by('-hits','-ratings','-date_time_create')
        else:
            return redirect('/allproduct')

class search_admin_product_list(generic.ListView):
    template_name='pages/search_admin_home.html'
    paginate_by=10
    def get_queryset(self):  # new
        query = self.request.GET.get("search_admin")
        if self.request.user.is_superuser:
            object_list = product.objects.filter(Q(title__icontains=query))
        elif self.request.user.is_author:
            object_list = product.objects.filter(owner=self.request.user).filter(Q(title__icontains=query))
        else:
            return redirect('/allproduct')
        return object_list


class profile(LoginRequiredMixin,generic.UpdateView):
    model=Customeuser
    template_name='pages/profile.html'
    form_class=profile_form
    success_url=reverse_lazy('admin_home')
    def get_object(self):
        return get_object_or_404(Customeuser,pk=self.request.user.pk)
    def get_form_kwargs(self):
        kwargs=super(profile,self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs

def password_change_done(request):
    return render(request,'account/password_change_done.html')