from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from vehicle.models import Vehicle


# Create your models here.
# PARKING SESSION MODEL
# class ParkingSession(models.Model):
#     vehicle = models.ForeignKey(
#         Vehicle, on_delete=models.CASCADE, related_name="parking_sessions"
#     )
#     receipt_number = models.CharField(max_length=20, unique=True, editable=False)
#     arrival_time = models.DateTimeField(default=timezone.now)
#     departure_time = models.DateTimeField(blank=True, null=True)
#     receiver_name = models.CharField(max_length=100, blank=True, null=True)
#     receiver_phone = models.CharField(max_length=10, blank=True, null=True)
#     receiver_nin = models.CharField(max_length=20, blank=True, null=True)
#     parking_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     is_signed_out = models.BooleanField(default=False)
#     created_by = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True, related_name="created_sessions"
#     )
#     signed_out_by = models.ForeignKey(
#         User,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="signed_out_sessions",
#     )
#     created_at = models.DateTimeField(auto_now_add=True)



