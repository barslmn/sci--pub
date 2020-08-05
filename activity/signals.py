from django.db.models.signals import post_save
from actstream import action
from django.contrib.auth.models import User

def user_save(sender, instance, created, **kwargs):
    action.send(instance, verb='was saved')

post_save.connect(user_save, sender=User)
