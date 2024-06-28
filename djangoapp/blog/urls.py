from django.urls import path
from blog.views import index, post, page, created_by, category

app_name = "blog"

urlpatterns = [
    path('', index, name="index"),
    path('post/<slug:slug>/', post, name="post"),
    path('page/<slug:slug>/', page, name="page"),
    path('created_by/<int:author_pk>/', created_by, name="created_by"),
    path('created_by/<slug:slug>/', category, name="category"),
]
