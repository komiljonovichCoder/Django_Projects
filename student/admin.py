from django.contrib import admin
from .models import Student, Category, GroupPost

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "time_created", "is_active")
    list_display_links = ("id", "name")
    ordering = ["id"]
    list_editable = ["is_active"]
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name", )
    ordering = ["id"]
    list_per_page = 5

@admin.register(GroupPost)
class GroupPostAdmin(admin.ModelAdmin):
    list_display = ("id", "group_name", "slug")
    list_display_links = ("id", "group_name")
    ordering = ["id"]
    list_editable = ["slug"]
    list_per_page = 5