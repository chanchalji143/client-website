from django.db import models


class Appointment(models.Model):

    SERVICE_CHOICES = [
        ('cleaning', 'Dental Cleaning'),
        ('whitening', 'Teeth Whitening'),
        ('root_canal', 'Root Canal Treatment'),
        ('implant', 'Dental Implants'),
        ('braces', 'Braces & Alignment'),
        ('kids', 'Kids Dentistry'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    date = models.DateField()

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    from django.db import models


class ClinicSettings(models.Model):
    logo = models.ImageField(upload_to='clinic/')

    def __str__(self):
        return "Clinic Settings"