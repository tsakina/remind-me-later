from django.db import models


class Reminder(models.Model):
    REMIND_BY_CHOICES = (
        ('email', 'Email'),
        ('sms', 'SMS'),
    )

    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    remind_by = models.CharField(max_length=10, choices=REMIND_BY_CHOICES)

    def __str__(self):
        return f"{self.message[:20]}... @ {self.date} {self.time}"
