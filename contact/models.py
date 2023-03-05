from datetime import datetime
from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    company = models.CharField(max_length=1000,blank=True)
    create_date = models.DateTimeField(blank=True, default = datetime.now)

    def __str__(self):
        return self.email
