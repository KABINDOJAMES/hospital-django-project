from django.contrib import admin
from .models import Service, Contact, Pharmacy, SocialMediaLinks, AboutUs, Home
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

admin.site.site_header = "UNITY MEDICAL CENTRE" 

class ServiceAdmin(SummernoteModelAdmin):
    list_display = ['title', 'date']
    search = ['title', 'body']
    list_filter = ['date']
    summernote_fields = ('body',)
    prepopulated_fields = {"slug": ("title",)}

class PharmacyAdmin(SummernoteModelAdmin):
    list_display = ['title', 'date']
    summernote_fields = ('body', )

class SocialMediaLinksAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    search = ['title']

class AboutUsAdmin(SummernoteModelAdmin):
    list_display = ['title']
    summernote_fields = ('body', )

class HomeAdmin(SummernoteModelAdmin):
    list_display = ['title']
    summernote_fields = ('body', )


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'subject']
    search = ['name', 'message']
    list_filter = ['date']

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Pharmacy, PharmacyAdmin)
admin.site.register(SocialMediaLinks, SocialMediaLinksAdmin)