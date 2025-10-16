from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title',
              'content',
              'preview',
              'is_published',
              ]
    template_name = "blog/add_article.html"
    success_url = reverse_lazy("blog:home")


class BlogListView(ListView):
    model = Blog
    # paginate_by = 3
    template_name = "blog/home.html"
    context_object_name = 'blog'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title',
              'content',
              'preview',
              'is_published',
              ]
    template_name = "blog/update_article.html"
    success_url = reverse_lazy("blog:home")


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog:home')
