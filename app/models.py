from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Task(models.Model):
    desc = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.desc

class TaskCompletionRecord(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    timestamp = models.DateField(default=models.functions.Now())
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task} on {self.timestamp} by {self.user}"

class HouseMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    iconchar = models.CharField(max_length=8)
    color_hex = models.CharField(
        max_length=7,  # Length includes the '#' symbol
        validators=[
            RegexValidator(
                regex=r'^#([A-Fa-f0-9]{6})$',
                message="Enter a valid hex color code (e.g., #AABBCC)."
            )
        ],
        default="#FFFFFF"
    )

    def __str__(self):
        return f"{self.user.username}: {self.iconchar}"
    
    def save(self, *args, **kwargs):
        self.iconchar = self.iconchar or self.user.username[0] # get first letter of the name
        super().save(*args, **kwargs)