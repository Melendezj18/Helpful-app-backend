# from django.db import models
# from django.contrib.auth import get_user_model

# class House(models.Model):
#     bedroom = models.IntegerField(max_length=100)
#     bathroom = models.IntegerField(max_length=100)
#     owner = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     # __str__
#     def __str__(self):
#         return f"{self.bedroom} {self.bathroom}"
