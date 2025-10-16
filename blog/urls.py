from django.urls import path

from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView

app_name = 'blog'

urlpatterns =[
    path("home/", BlogListView.as_view(), name="home"),
    path("add_article/", BlogCreateView.as_view(), name="add_article"),
    path("update_article/<int:pk>/edit/", BlogUpdateView.as_view(), name="update_article"),
    path("blog_confirm_delete/<int:pk>/delete", BlogDeleteView.as_view(), name="blog_confirm_delete"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]