from django.contrib import admin
from .models import Student, Category, GroupPost

admin.site.register([Student, Category, GroupPost])
