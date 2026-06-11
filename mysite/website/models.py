from django.db import models
class Doctor(models.Model):
    name = models.CharField(max_length=100)

    email = models.EmailField(null=True, blank=True)

    experience = models.IntegerField(null=True, blank=True)

    image = models.CharField(max_length=255, null=True, blank=True)

    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name}"