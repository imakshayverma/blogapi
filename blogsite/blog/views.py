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
    The list populated is paginated with with a size of 5 post per page."

    Returns
    ========
    A JSON object with all the list of 5 blog posts.  
    Example : 
    {
        "count": 18,
        "next": "http://127.0.0.1:8000/blog/?page=2",
        "previous": null,
        "results": [
            {
                "id": "0e350770-4c29-45a5-963f-6fb5a7570a78",
                "title": "Post Title",
                "content": [
                    {
                        "id": 50,
                        "content": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32.",
                        "sequence": 1
                    },
                    ...
                ]
            }
    """
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostListSetPagination
    lookup_field = 'id'

class PostCreateAPIView(CreateAPIView):
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'Message' : 'Blog Successfully Added', 'status' : status.HTTP_201_CREATED }, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'Message' : "Input Data is improper. Please refer to the documentation for the right format", 'status' : status.HTTP_400_BAD_REQUEST})

class PostShowAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostShowSerializer
    lookup_field = 'id'

class CommentCreateAPIView(CreateAPIView):
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