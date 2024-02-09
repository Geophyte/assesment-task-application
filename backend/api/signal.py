from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.sessions.models import Session
from django.utils import timezone

@receiver(pre_delete, sender=User)
def delete_user_sessions(sender, instance, **kwargs):
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now(),
                                             session_data__contains=instance.pk)

    for session in active_sessions:
        session.delete()
