from django.db import models
import datetime
from django.utils import timezone


class Control(models.Model):
    control_number = models.CharField(max_length=10)
    control_type = models.CharField(max_length=20)
    control_name = models.TextField()
    control_set_version_number = models.CharField(max_length=20)
    authorization_package_name = models.TextField()
    allocation_status = models.CharField(max_length=60)
    overall_update_date =  models.DateTimeField(null=True, blank=True)
    overall_control_status = models.CharField(max_length=60)
    assessment_status = models.CharField(max_length=60)
    tracking_id = models.CharField(max_length=60)

class ArsBaseline(models.Model):
    ars_baseline = models.CharField(max_length=10)
    control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name='control')


