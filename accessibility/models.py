"""
accessibility/models.py
"""

from django.db import models

from accessibility.accessibility import ACCESSBILITY_FEATURE
from horilla.models import HorillaModel


class DefaultAccessibility(HorillaModel):
    """
    DefaultAccessibilityModel
    """

    
    class Meta:
        db_table = 'ERP_HR_Accessibility_DefaultAccessibility'

    feature = models.CharField(max_length=100, choices=ACCESSBILITY_FEATURE)
    filter = models.JSONField()
    exclude_all = models.BooleanField(default=False)
