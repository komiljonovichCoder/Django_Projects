from django.shortcuts import render, get_object_or_404
from .models import *

data = {
        'title':"Student Management",
        'page': "Dashboard",
        'students': Student.objects.filter(is_active=True),
        'categories': Category.objects.all(),
        'groups': GroupPost.objects.all(),
    }

def index(request):    
    return render(request, 'student/index.html', context=data)

def show_post(request, post_slug):
    data['student'] = get_object_or_404(Student, slug=post_slug)
    return render(request,'student/show_post.html', context=data)

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    data['students'] = category.categories.filter(is_active=True)
    data['page'] = f"Student {category.name}"
    return render(request,'student/index.html', context=data)

def show_group(request, group_slug):
    group = get_object_or_404(GroupPost, slug=group_slug)
    data['students'] = group.group_students.filter(is_active=True)
    data['page'] = f"Student {group.group_name}"
    return render(request,'student/index.html', context=data)
