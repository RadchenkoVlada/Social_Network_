from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Post
from .serializers import PostSerializer


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get('post')

        # Create a post from the above data
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"success": "Post '{}' created successfully".format(post_saved.title)})


    def put(self, request, pk):
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data.get('post')
        serializer = PostSerializer(instance=saved_post, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()

        return Response({
            "success": "Post '{}' updated successfully".format(post_saved.title)
        })

    def delete (self, request, pk):
        # Get object with this pk
        post = get_object_or_404(Post.objects.all(), pk=pk)
        post.delete()
        return Response({
            "message": "Post with id `{}` has been deleted.".format(pk)
        }, status=204)
