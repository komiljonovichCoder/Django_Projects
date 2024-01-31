from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('post/<slug:post_slug>/', show_post, name="student_post"),
    path('cat/<slug:cat_slug>/', show_category, name="category"),
    path('group/<slug:group_slug>/', show_group, name="group"),
]
