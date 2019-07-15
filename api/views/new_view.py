from api.models import Review
from api.serializers import ReviewSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ReviewListCreate(APIView):
    permission_class = (IsAuthenticated,)

    def get(self, request):
        if request.user.is_superuser:
            reviews = Review.objects.all()
        else:
            reviews = Review.objects.filter(created_by=request.user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["ip_address"] = ip
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ReviewDetail(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(id=pk)
        except Review.DoesNotExist as e:
            raise e

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
