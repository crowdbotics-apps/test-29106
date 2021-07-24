from django.conf import settings
from django.db import models


class Tasks(models.Model):
    "Generated Model"
    task_name = models.TextField()
