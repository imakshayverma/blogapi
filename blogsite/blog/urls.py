from django.conf.urls import url
from django.contrib import admin
from blog.views import (
	PostListAPIView, 
	PostShowAPIView, 
	PostCreateAPIView, 
	CommentCreateAPIView
	)

urlpatterns = [
	url(r'^$', PostListAPIView.as_view() ,name='list_blog'),
    url(r'^add/$', PostCreateAPIView.as_view() , name='add_blog'),
    url(r'^(?P<id>[\w-]+)/$', PostShowAPIView.as_view(), name='show_blog'),
    url(r'^(?P<id>[\w-]+)/add_comment/$', CommentCreateAPIView.as_view(), name='add_comment'), 
]