from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.forms import MyPostForm
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from datetime import datetime


class PostListView(ListView):
    published = Post.objects.exclude(published_date__exact=None)
    queryset = published.order_by("-published_date")
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"

    def get(self, request, *args, **kwargs):
        try:
            post = self.get_object()
        except Post.DoesNotExist:
            raise Http404
        context = {"object": post}
        return render(request, "blogging/detail.html", context)

def add_model(request):
    if request.method == 'POST':
        form = MyPostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.published_date = datetime.now()
            model_instance.save()
            return redirect('/')
    else:
        form = MyPostForm()
        return render(request, "blogging/add.html", {'form':form})
 

