from rest_framework import serializers
from django.utils import timezone
from .models import Post




class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    created_date = serializers.DateTimeField(default=timezone.now)
    published_date = serializers.DateTimeField(default=timezone.now)
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance
