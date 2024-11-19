from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateTimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f'Reservation for {self.name} on {self.date}'

