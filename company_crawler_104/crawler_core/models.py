from django.db import models
from django.utils import timezone


class result_list(models.Model):
    company_id = models.CharField(
        max_length = 255, 
        blank = False, 
        null = False, 
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
    user_selected = models.BooleanField(
        blank = True, 
        default = False, 
        )
  

class selected_list(models.Model):

    list_id = models.DateTimeField(default = timezone.now)
    company_id = models.CharField(max_length = 255, blank = False, null = False)
    company_name = models.CharField(max_length = 255, blank = False, null = False)
    company_profile = models.TextField(blank = True, null = False)
    company_product = models.TextField(blank = True, null = True)
    user_note = models.TextField(blank = True, null = True)
    create_date = models.DateTimeField(default = timezone.now)


