from django.urls import path
from blogging.views import PostDetailView, PostListView, add_model

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("add/", add_model, name="add_post"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
]
