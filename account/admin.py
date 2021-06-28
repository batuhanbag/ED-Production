from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email','fullName','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','fullName')
    

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    

admin.site.register(Account, AccountAdmin)