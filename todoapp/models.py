from django.db import models

# Create your models here.
class todoModel(models.Model):
    task_title = models.CharField(max_length = 50)
    is_done = models.BooleanField(default = False)