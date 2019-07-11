from django.test import TestCase
from api.models import Review, Company
from api.serializers import ReviewSerializer2
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

client = APIClient()
TEST_USER = 'admin'


class UserTest(TestCase):
    @staticmethod
    def get_or_create_user(check_username=TEST_USER):
        user, _ = User.objects.get_or_create(username=check_username)
        user.is_active = True
        user.save()
        return user

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)


class ReviewTest(ModelTest):
    def test_Review_list(self):
        response = self.client.get(reverse('Review-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Review_detail(self):
        r_objs = Review.objects.all()
        if r_objs:
            response = self.client.get(reverse('Review-detail', args=[r_objs[0].id]), format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)


class CompanyTest(TestCase):
    def test_Review_list(self):
        response = self.client.get(reverse('Company-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Review_detail(self):
        c_objs = Company.objects.all()
        if c_objs:
            response = self.client.get(reverse('Review-detail', args=[c_objs[0].id]), format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)


class SerializerTest(ModelTest):
    def test_serializer(self):
        review = self.review
        serializer = ReviewSerializer2(review)
        self.assertEqual(serializer.data['rating'], review.rating)
        self.assertEqual(serializer.data['title'], review.title)
        self.assertEqual(serializer.data['summary'], review.summary)
        self.assertEqual(serializer.data['created_at'], review.created_at)
        self.assertEqual(serializer.data['company'], review.company)
        self.assertEqual(serializer.data['created_ by'], review.created_by)