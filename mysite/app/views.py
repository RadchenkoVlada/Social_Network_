from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Post
from .models import User

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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # if serializer.is_valid(raise_exception=True):
        #     post_saved = serializer.save()
        #     return Response({"success": "Post '{}' created successfully".format(post_saved.title)})


    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data.get('post')
        serializer = PostSerializer(instance=saved_post, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
            return Response({
                "success": "Post '{}' updated successfully".format(post_saved.title)})
        else:
            return Response({"fail": "'{}'".format(serializer.errors)})

    def delete (self, request, pk):
        # Get object with this pk
        post = get_object_or_404(Post.objects.all(), pk=pk)
        post.delete()
        return Response({
            "message": "Post with id `{}` has been deleted.".format(pk)
        }, status=204)
