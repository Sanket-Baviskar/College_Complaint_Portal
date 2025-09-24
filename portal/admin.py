from django.contrib import admin
from .models import Department, Complaint

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id','title','department','user','status','priority','created_at')
    list_filter = ('status','priority','department')
    search_fields = ('title','description','user__username')
