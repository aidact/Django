from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Review


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ReviewSerializer2(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # rating = serializers.IntegerField(required=True)
    # title = serializers.CharField(required=True)
    # summary = serializers.CharField(required=True)
    # created_at = serializers.DateTimeField()
    # company = CompanySerializer()
    # created_by = UserSerializer()

    class Meta:
        model = Review
        fields = ('id', 'rating', 'title', 'summary', 'created_at', 'company', 'created_by',)


