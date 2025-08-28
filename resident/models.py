from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from .utility import generate_code


# Create your models here.


class User(AbstractUser):
    is_resident = models.BooleanField(default=False)
    is_security = models.BooleanField(default=False)
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

class House(models.Model):
    house_number = models.PositiveIntegerField(blank=False, null=False)
    address = models.CharField(max_length=255, blank= False, null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class Invite(models.Model):
    code = models.CharField(max_length=6, unique=True, default = generate_code())
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null = False, blank = False)
    status = models.BooleanField(default = True)
    house = models.ForeignKey(House, on_delete=models.PROTECT)


class Visitor(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=11, blank=False, null=False)
    invite= models.ForeignKey(Invite, on_delete=models.PROTECT)
