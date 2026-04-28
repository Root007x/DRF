from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime


APPOINTMENT_STATUS = [
    ("Pending", "Pending"),
    ("Completed", "Completed"),
    ("Running", "Running"),
]

APPOINTMENT_TYPES = [
    ("Online", "Online"),
    ("Offline", "Offline"),
]


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(choices=APPOINTMENT_TYPES, max_length=20)
    appointment_status = models.CharField(
        choices=APPOINTMENT_STATUS, max_length=20, default="Pending"
    )
    symptoms = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name}, Patient: {self.patient.user.last_name}"
