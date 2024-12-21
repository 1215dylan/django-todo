from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=200)#CharField字串
    completed=models.BooleanField(default=False)#BooleanField布林
    
    def __str__(self):
        return self.title
