from django.db import models

class Student(models.Model):
    sur_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)



