from django.test import TestCase
from api.models import Review, Company
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User

client = APIClient()
TEST_USER = 'admin2'

REVIEW_RATING = 4
REVIEW_TITLE = 'Good'
REVIEW_SUMMARY = 'Good'

COMPANY_NAME = 'Company 3'


class BaseTest(TestCase):
    @staticmethod
    def get_or_create_user(check_username=TEST_USER):
        user, _ = User.objects.get_or_create(username=check_username)
        user.is_active = True
        user.save()
        return user

    @classmethod
    def setUp(cls):
        cls.user = BaseTest.get_or_create_user(TEST_USER)
        cls.company = Company.objects.create(name=COMPANY_NAME)
        cls.review = Review.objects.create(rating=REVIEW_RATING, title=REVIEW_TITLE, summary=REVIEW_SUMMARY,
                                           company=cls.company, created_by=cls.user)


class ReviewModelTest(BaseTest):
    def test_fields(self):
        review = self.review
        self.assertEqual(review.rating, REVIEW_RATING)
        self.assertEqual(review.title, REVIEW_TITLE)
        self.assertEqual(review.summary, REVIEW_SUMMARY)
        self.assertEqual(review.company, self.company)
        self.assertEqual(review.created_by, self.user)

    def test_str(self):
        self.assertEqual(self.review.__str__(), '{}: {} {} {}'.format(self.review.id, self.review.rating, self.review.title, self.review.summary))


class CompanyModelTest(BaseTest):
    def test_fields(self):
        company = self.company
        self.assertEqual(company.name, COMPANY_NAME)

    def test_str(self):
        self.assertEqual(self.company.__str__(), '{}: {}'.format(self.company.id, self.company.name))

