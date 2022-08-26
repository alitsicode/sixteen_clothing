from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from . models import Customeuser

class customusercreationform(UserCreationForm):
    class Meta:
        model=Customeuser
        fields=UserCreationForm.Meta.fields + ('age','avatar')

class customuserchangeform(UserChangeForm):
    class Meta:
        model=Customeuser
        fields=UserChangeForm.Meta.fields