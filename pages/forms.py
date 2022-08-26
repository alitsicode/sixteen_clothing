from django import forms
# from .models import comment
from accounts.models import Customeuser
# class productcomment(forms.ModelForm):
#     class Meta:
#         model=comment
#         fields=('comment_text','is_suggest',)

class profile_form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(profile_form,self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['first_name'].disabled=True
            self.fields['last_name'].disabled=True
            self.fields['is_staff'].disabled=True
            self.fields['date_joined'].disabled=True
            self.fields['is_author'].disabled=True
        self.fields['is_staff'].help_text=None
    class Meta:
        model= Customeuser
        fields=['username','first_name','last_name','avatar','email','date_joined','age','is_staff','is_author']