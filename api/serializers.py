from rest_framework import serializers
from api.models import Review
from django.utils import timezone


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rating = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True)
    summary = serializers.CharField(required=True)

    def create(self, validated_data):
        review = Review(**validated_data)
        review.save()
        return review

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.title = validated_data.get('title', instance.title)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.save()
        return instance


class ReviewSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    rating = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True)
    summary = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(default=timezone.now())
    company = CompanySerializer()

    class Meta:
        model = Review
        fields = ('id', 'rating', 'title', 'summary')
