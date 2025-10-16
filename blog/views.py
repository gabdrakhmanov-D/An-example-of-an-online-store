from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    paginate_by = 5
    template_name = "blog/home.html"
    context_object_name = 'blogs'


class BlogUpdateView(UpdateView):

    model = Blog
    fields = ['title',
              'content',
              'preview',
              'is_published',
              ]
    template_name = "blog/update_article.html"

    def form_valid(self, form):
        page = self.get_context_data()['object'].pk
        self.success_url = reverse_lazy('blog:blog_detail', kwargs={'pk': page})
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:home')


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj
