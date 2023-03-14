from django.db import models
from django.contrib.auth import get_user_model

class House(models.Model):
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # __str__
    def __str__(self):
        return f"{self.bedroom} {self.bathroom}"

    def as_dict(self):
        """Returns dictionary version of House models"""
        return {
            'id': self.id,
            'bedroom': self.bedroom,
            'bathroom': self.bathroom,
            'owner': self.owner.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }