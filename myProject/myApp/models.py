from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=300, unique=True)
    phone_Number = models.IntegerField()

    def __str__(self):
        return self.name