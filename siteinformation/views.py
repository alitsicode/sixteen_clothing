from django.shortcuts import render
from django.views import generic
from .models import contactmessage,aboutus_information
from django.contrib import messages
# Create your views here.

class contactus(generic.CreateView):
    model= contactmessage
    template_name='siteinformation/contact.html'
    fields=['subject','body']
    success_url='/allproduct'
    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.author=self.request.user
        instance.save()
        messages.success(self.request, "your message successfuly send to us (:")
        return super().form_valid(form)

def aboutus(request):
    aboutinfo=aboutus_information.objects.all().last()
    return render(request,'siteinformation/about.html',context={'about':aboutinfo})