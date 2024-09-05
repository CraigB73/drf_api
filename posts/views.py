from rest_framework.views import APIView
from .models import Post
from rest_framework.response import Response
from .serializer import PostSerializer

# Create your views here.
class PostList(APIView):
     def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True, context={'request': request})
        return Response(serializer.data)