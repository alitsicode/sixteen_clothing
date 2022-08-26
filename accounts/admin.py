from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import customusercreationform,customuserchangeform
from accounts.models import Customeuser
# Register your models here.
class customuseradmin(UserAdmin):
    add_form=customusercreationform
    form=customuserchangeform
    model=Customeuser
    fieldsets=UserAdmin.fieldsets+(
        (None,{'fields':('age','is_author','avatar')},),
    )
    add_fieldsets=UserAdmin.add_fieldsets+(
        (None,{'fields':('age','is_author','avatar')},),
    )
admin.site.register(Customeuser,customuseradmin)