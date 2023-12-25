from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Customer, Shop


@receiver(post_delete, sender=Customer)
def delete_user_when_customer_deleted(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()


@receiver(post_delete, sender=Shop)
def delete_user_when_shop_deleted(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()
