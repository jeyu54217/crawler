from django.db import models
from django.utils import timezone

class result_list(models.Model):
    company_id = models.CharField(
        max_length = 255, 
        blank = False, 
        null = True, 
        )
    company_name = models.CharField(
        max_length = 255, 
        blank = False, 
        null = False, 
        )
    company_profile = models.TextField(
        blank = True, 
        null = False, 
        )
    company_product = models.TextField(
        blank = True, 
        null = True, 
        )
    user_note = models.TextField(
        blank = True, 
        null = True, 
        default = "",
        )
    create_date = models.DateTimeField(
        default = timezone.now
        )
   