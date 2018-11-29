from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset()#.filter(city='kolk')

class UserProfile(models.Model):
    # User test information (Not production fields)
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    current_upload = models.FileField(upload_to='uploads/', blank=True)
    previous_upload = models.FileField(upload_to='uploads/', blank=True)
    upload_changes = models.FileField(upload_to='uploads/', blank=True)

    test = UserProfileManager() #test custom model manager query

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])



post_save.connect(create_profile, sender=User)