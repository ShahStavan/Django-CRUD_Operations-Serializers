from django.db import models

# Create your models here.

class reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField()
    reporter = models.ForeignKey(reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

