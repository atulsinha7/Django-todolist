from django.db import models

# Create your models here.
class users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    comp = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class checklist(models.Model):
    taskname = models.TextField()
    uid = models.ForeignKey(users, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.taskname

