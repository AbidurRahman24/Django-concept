from django.db import models

# Create your models here.
class students(models.Model):
    Name = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 50)
    Age = models.IntegerField(default = 1)
    Dept = models.CharField(max_length = 50)
    def __str__(self):
        return self.Name + " " + self.Dept