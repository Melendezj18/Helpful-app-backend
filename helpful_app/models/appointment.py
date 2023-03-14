from django.db import models


class Appointment(models.Model):
    time = models.TimeField()
    date = models.DateField()
    address = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date} at {self.time} - {self.address}"
    
    def as_dict(self):
        """Returns dictionary version of Appointment models"""
        return {
            'id': self.id,
            'time': self.time,
            'date': self.date,
            'address': self.address,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
