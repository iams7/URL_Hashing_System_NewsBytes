from django.db import models
from django.db.models import base

# Models to represent database fields
# Django automatically-generated database-access API


# User Model for Authentication (optional)
class User(models.Model):

    user_id = models.CharField(max_length=64, unique=True)  # Eg. 14MSE1007
    user_name = models.CharField(max_length=256)  # MS Dhoni
    user_email = models.EmailField(max_length=256)  # msd@bot.com
    user_password = models.CharField(max_length=256)


# UTM Parameters Model for
class UTMParameter(models.Model):

    website_url = models.CharField(max_length=256)  # Eg. newsbytesapp.com
    campaign_source = models.CharField(max_length=256)  # linkedin
    campaign_medium = models.CharField(max_length=256)  # profile
    campaign_term = models.CharField(max_length=256)  # organic
    campaign_content = models.CharField(max_length=256)  # 39
    campaign_name = models.CharField(max_length=256)  # Course

    campaign_url = models.CharField(
        max_length=1024, blank=True)
    campaign_hashed_url = models.CharField(
        max_length=256, blank=True)

    # return a string value to the database (instead of an object id)
    def __str__(self):

        return f"{self.website_url}"
