from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('username', 'firstname', 'lastname', 'type', 'is_admin', 'is_staff','is_active','password')
    search_fields = ('username', 'firstname', 'lastname')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)