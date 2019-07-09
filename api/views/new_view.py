from django.contrib.auth.models import User
from api.models import Review
from api.serializers import ReviewSerializer2, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer2(reviews, many=True)
        return Response(serializer.data)

    def post(self):
        serializer = ReviewSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ReviewDetail(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(id=pk)
        except Review.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer2(review)
        return Response(serializer.data)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response("deleted")


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
