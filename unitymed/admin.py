from django.contrib import admin
from .models import Service, Contact
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

admin.site.site_header = "UNITY MEDICAL CENTRE" 

class ServiceAdmin(SummernoteModelAdmin):
    list_display = ['title', 'date']
    search = ['title', 'body']
    list_filter = ['date']
    summernote_fields = ('body',)
    prepopulated_fields = {"slug": ("title",)}

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'subject']
    search = ['name', 'message']
    list_filter = ['date']


admin.site.register(Service, ServiceAdmin)
admin.site.register(Contact, ContactAdmin)