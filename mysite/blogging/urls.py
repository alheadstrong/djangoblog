from django.urls import path
from blogging.views import detail_view, list_view, add_Post

urlpatterns = [
        path('', list_view, name="blog_index"),
        path('add/', add_Post, name="blog_add"),
        path('posts/<int:post_id>/', detail_view, name="blog_detail"),
        ]

