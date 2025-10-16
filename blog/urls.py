from django.urls import path

from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns =[
    path("home/", BlogListView.as_view(), name="home"),
    path("add_article/", BlogCreateView.as_view(), name="add_article"),
    path("update_article/<int:pk>", BlogUpdateView.as_view(), name="update_article"),
    path("blog_confirm_delete/<int:pk>", BlogDeleteView.as_view(), name="blog_confirm_delete"),
]