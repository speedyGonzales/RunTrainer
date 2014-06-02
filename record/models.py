from django.db import models

# Create your models here.
class Record(models.Model):
    description=models.TextField()
    distance=models.IntegerField()
    reg_date=models.DateTimeField('date published')
    reg_user=models.IntegerField()


