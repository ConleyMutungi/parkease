from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Vehicle(models.Model):

    VEHICLE_TYPES = [
        ("truck", "Truck"),
        ("car", "Personal Car"),
        ("taxi", "Taxi"),
        ("coaster", "Coaster"),
        ("boda", "Boda-boda"),
    ]

    ugandan_phone_validator = RegexValidator(
    regex=r'^(\+256|0)(7)\d{8}$',
    message="Enter a valid Ugandan number: 07XXXXXXXXX or +2567XXXXXXXX"
)
    nin_validator = RegexValidator(
    regex=r'^(CM|CF)[A-Z0-9]{10,}$',
    message="NIN must start with CM (male) or CF (female)"
)

    driver_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, validators=[ugandan_phone_validator])
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    model = models.CharField(max_length=100)
    number_plate = models.CharField(
        max_length=10,
        unique=True,
    )
    color = models.CharField(max_length=50)
    nin = models.CharField(max_length=20, blank=True, null=True, validators=[nin_validator])
    

    def __str__(self):
        return self.name

