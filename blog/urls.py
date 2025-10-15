from django.urls import path

from blog.views import BlogListView, BlogCreateView

app_name = 'blog'

urlpatterns =[
    path("home/", BlogListView.as_view(), name="home"),
    path("add_article/", BlogCreateView.as_view(), name="add_article"),
]