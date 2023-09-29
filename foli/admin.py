from django.contrib import admin
from . models import Contact, Project, Member, Service
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'client', 'description']
    list_filter = ['name', 'date', 'client']
    search_fields = ['name', 'date', 'client']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone','message']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
