from django.contrib import admin
from formApp.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'message')

admin.site.register(User, UserAdmin)