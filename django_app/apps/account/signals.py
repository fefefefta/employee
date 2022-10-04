from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, Wallet
from ..board.models import Payment


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)


@receiver(post_save, sender=Payment)
def update_user_wallet_balance(sender, instance, created, **kwargs):
    user = Payment.objects.get(id=instance.id).user
    payment = Payment.objects.get(id=instance.id).payment
    user.wallet.balance += payment
    user.save()
