import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Review
from api.serializers import ReviewSerializer, ReviewSerializer2, CompanySerializer


@csrf_exempt
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer2(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = ReviewSerializer2(data=data)
        # review = Review()
        # review.rating = data.get('rating', '')
        # review.title = data.get('title', '')
        # review.summary = data.get('summary', '')
        # review.created_at = data.get('date', '')
        # review.company = data.get('company', '')
        # review.save()
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})


# reviews = company.review_set.all()

@csrf_exempt
def review_detail(request, pk):
    try:
        review = Review.objects.get(id=pk)
    except Review.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = ReviewSerializer(instance=review, data=data)
        # review.rating = data.get('rating', review.rating)
        # review.title = data.get('title', review.title)
        # review.summary = data.get('summary', review.summary)
        # review.save()
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        review.delete()
        return JsonResponse({'delete': True})
    return JsonResponse({'error': 'bad request'})
