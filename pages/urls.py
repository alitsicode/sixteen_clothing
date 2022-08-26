from django.urls import path
from . import views

urlpatterns = [
   path('',views.homeprouct,name='homeproduct'),
   path('allproduct',views.listshop.as_view(),name='listproduct'),
   path('detail/<int:pk>',views.detailshop,name='detailproduct'),
   path('create',views.createshop.as_view(),name='createproduct'),
   path('update/<int:pk>',views.updateshop.as_view(),name='updateproduct'),
   path('delete/<int:pk>',views.deleteshop.as_view(),name='deleteproduct'),
   path('like/<int:pk>',views.like,name='likeproduct'),
   path('save_post/<int:pk>',views.save_post,name='saveproduct'),
   path('bookmark/',views.bookmark.as_view(),name='bookmarkproduct'),
   path('search/',views.search.as_view(),name='searchproduct'),
   path('filter/',views.filter_product.as_view(),name='filterproduct'),
   path('filterprice/',views.filter_by_price.as_view(),name='filterbyprice'),
   path('user_post/<int:pk>',views.user_each_post,name='user_post'),
   path('admin_home/',views.admin_product_list.as_view(),name='admin_home'),
   path('admin_search/',views.search_admin_product_list.as_view(),name='admin_search'),
   path('profile/',views.profile.as_view(),name='profile'),
   path('password_change_done/',views.password_change_done,name='password_change_done'),
]