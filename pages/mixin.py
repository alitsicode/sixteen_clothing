from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import product
class fieldmixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields=['title','description','price','owner','cover','is_published','stock']
        elif request.user.is_author:
            self.fields=['title','description','price','cover']
        else:
            raise Http404('you cant see this page')
        return super().dispatch(request, *args, **kwargs)

class authormixin():
    def dispatch(self, request,pk, *args, **kwargs):
        products=get_object_or_404(product,pk=pk)
        if products.owner==request.user and products.is_published in ['d','b'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('you cant see this page')
class superusermixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('you cant see this page')