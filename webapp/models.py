from django.db import models

# Create your models here.


class employees(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    employees_id = models.IntegerField()

    def __str__(self):
        return self.first_name
    