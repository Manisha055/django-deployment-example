from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Directly Not Able to Inherit User model for inherit need to use OneToOneField
    user=models.OneToOneField(User,on_delete=models.CASCADE,)

    # Addition Attribute

    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username