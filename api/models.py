from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'rating': self.name,
        }


class Review(models.Model):
    rating = models.PositiveIntegerField()
    title = models.CharField(max_length=64)
    summary = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '{}: {}'.format(self.id, self.rating, self.title, self.summary)

    def to_json(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'title': self.title,
            'summary': self.summary,
            'publication time': self.created_at,
            'company': '{}'.format(self.company),
        }