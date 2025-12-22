from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.goals.models import Goal
from .models import Notification

@receiver(post_save, sender=Goal)
def notify_goal_update(sender, instance, created, **kwargs):
    # Notify when a goal is created OR completed
    if created:
        message = f"Goal Created: {instance.title}"
    elif instance.is_completed:
        message = f"Goal Completed! Well done: {instance.title}"
    else:
        return

    Notification.objects.create(user=instance.user, message=message)
