from rest_framework import status
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    CreateAPIView
    )
from .serializers import (
    PostListSerializer, 
    PostSerializer, 
    PostShowSerializer, 
    CommentSerializer
    )
from rest_framework.response import Response
from .models import Post, Paragraph
from blog.pagination import PostListSetPagination

# Create your views here.
class PostListAPIView(ListAPIView):
    """
    API endpoint that allows users to be list all the blog post available. 
    The populated list is paginated with a size of 5 post per page."
    """
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostListSetPagination
    lookup_field = 'id'

class PostCreateAPIView(CreateAPIView):
    """
    API endpoint that allows users add a blog post. 
    Require a Title and Text to create a post. 
    """
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'Message' : 'Blog Successfully Added', 'status' : status.HTTP_201_CREATED }, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'Message' : "Input Data is in incorrect format. Please refer to the documentation for the right format", 'status' : status.HTTP_400_BAD_REQUEST})

class PostShowAPIView(RetrieveAPIView):
    """
    API endpoint that details out a single blog post refered using a unique identifier.
    """
    queryset = Post.objects.all()
    serializer_class = PostShowSerializer
    lookup_field = 'id'

class CommentCreateAPIView(CreateAPIView):
    """
    API endpoint that allows users to comment on a paragraph in a blog post.
    Requires a paragraph id and the comment text to create a comment.  
    """
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(para_id = Paragraph.objects.get(id = self.request.data.get("para_id")))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'Message' : 'Comment Successfully Added', 'status' : status.HTTP_201_CREATED }, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'Message' : "Input Data is improper. Please refer to the documentation for the right format", 'status' : status.HTTP_400_BAD_REQUEST})