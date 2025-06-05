from typing import Iterable
from django.db import models
from utils.constants import PHONE_NUMBER_VALIDATOR

class ContactMeEmail(models.Model):
    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Email\'s'

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=17,
        validators=[PHONE_NUMBER_VALIDATOR],
        blank=True, null=True)
    subject = models.CharField(max_length=160)
    message = models.TextField()
    
    email_send = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'

