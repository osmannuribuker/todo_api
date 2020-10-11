from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "{} - {}".format(str(self.id), self.title)
    
    def what_is_task(self):
        return 'Task is "{}"'.format(self.title)
