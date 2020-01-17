from django.db import models
# from django_countries.fields import CountryField
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('First Name', max_length=10, null=True, blank=True)
    last_name = models.CharField('Last Name', max_length=10, null=True, blank=True)
    email_id = models.EmailField('Email Id', max_length=20, null=True, blank=True)
    mobile_number = models.CharField('Mobile No', max_length=10, validators=[MinLengthValidator(10)], null=True, blank=True)
    photo = models.ImageField('Photo', upload_to='profile_pics', blank=True)
    street = models.CharField('Street', max_length=50, null=True, blank=True)
    country = models.CharField('Mobile No', max_length=10, null=True, blank=True)
    state = models.CharField('State', max_length=10, null=True, blank=True)
    city = models.CharField('City', max_length=10, null=True, blank=True)
    # country_new = CountryField()

    def __str__(self):
        return self.first_name

