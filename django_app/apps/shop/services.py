from apps.account.models import Wallet


def buy_with_coins(user_id, price):
    """Покупка товара за монеты"""
    wallet = Wallet.objects.get(id=user_id)

    if wallet.balance >= price:
        wallet.balance -= price
        wallet.save()

    if wallet.balance < price:
        raise ValueError("Недостаточно монет")


def buy_with_certificate():
    """Покупка товара за сертификаты"""
    pass
