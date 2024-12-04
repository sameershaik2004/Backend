from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default="OPEN")

    def __str__(self):
        return self.title
