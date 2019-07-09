from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Review(models.Model):
    rating = models.PositiveIntegerField()
    title = models.CharField(max_length=64)
    summary = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='date')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '{}: {}'.format(self.id, self.rating, self.title, self.summary)
