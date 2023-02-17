from .models import Topics
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

def updateTopic(sender, instance, created, **kwargs):
    if created == False:
        print(f"This topic: {instance} was updated!")
    else:
        print(f"This topic: {instance} was created!")

post_save.connect(updateTopic, sender=Topics)

@receiver(post_delete, sender=Topics)
def deleteTopic(sender, instance, **kwargs):
    print(f"Topic: {instance} was deleted!")