from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post

class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response({"posts": posts})
