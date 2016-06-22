from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Chirp(models.Model):
    body = models.CharField(max_length=141)
    created = models.DateTimeField(auto_now_add=True)
    bird = models.ForeignKey("auth.User")

    class Meta:
        ordering =["-created"]


class StopWord(models.Model):
    word = models.CharField(max_length=26)

class Profile(models.Model):
    user = models.OneToOneField("auth.user")
    # at this state model doens't do anything just would exist if migrate
    favorite_bird = models.CharField(max_length=100, null=True)

@receiver(post_save, sender=StopWord)  #- this is signal receiver fxn
def say_hello(**kwargs):
    print("hello world!")

@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance") # add as many fields as want on profile
    if created:
        Profile.objects.create(user=instance)

## - could calculate the avg for movie rating here in models.py
