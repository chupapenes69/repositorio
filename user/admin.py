from django.contrib import admin
from user.models import User

# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name','avatar','rol']
    ordering=['id']
    search_fields = ['first_name']

admin.site.register(User,userAdmin)