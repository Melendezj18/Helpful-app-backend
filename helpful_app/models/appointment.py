from django.db import models
from django.contrib.auth import get_user_model
from .house import House


class Appointment(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    time = models.TimeField()
    date = models.DateField()
    address = models.CharField(max_length=300)
    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date} at {self.time} - {self.address} - {self.house}"
    
    def as_dict(self):
        """Returns dictionary version of Appointment models"""
        return {
            'id': self.id,
            'owner': self.owner.id,
            'time': self.time,
            'date': self.date,
            'address': self.address,
            'house': self.house.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
