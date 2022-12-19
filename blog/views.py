from django.shortcuts import render
from  django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import BlogP
from django.urls import reverse_lazy , reverse

# Create your views here.

class HomeBlogView(ListView):
    model = BlogP
    template_name = "home.html"
    #context_object_name = "all_post_lists"

class DetailBlogView(DetailView):
    model = BlogP
    template_name = 'post_detail.html'

class CreatBlogView(CreateView):
    model = BlogP
    template_name = 'create_view.html'
    fields = ['title', 'author', 'body']

class EditBlogPost(UpdateView):
    model = BlogP
    template_name = 'edit_post.html'
    fields = ['title', 'body']



class DelBlogP(DeleteView):
    model =  BlogP
    template_name = "del_blogp.html"
    success_url = reverse_lazy('home')


