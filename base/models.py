from django.db import models
from django.db.models.deletion import CASCADE, RestrictedError
from django.contrib.auth.models import User


RACE_CHOICES = {
    ('800m', '800m'),
    ('mile', '1600m'),
    ('5k', '5k'),
    ('half-marathon', 'Half Marathon'),
    ('marathon', 'Marathon'),
}
# Create your models here.
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    instructions = models.TextField(null = True, blank = True)
    mileage = models.DecimalField(decimal_places = 1, max_digits = 3 ,null = True, blank = True)
    race_type =models.CharField(max_length = 100, choices = RACE_CHOICES, default = '5k')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['race_type']
    
    
