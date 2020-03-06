from django import template
from users.models import Cart
register = template.Library()

@register.filter
def center_in_cart(cart, center):
    #cart = Cart.objects.get(user=user)
    try:
        center = cart.centers.get(id=center)
        if center is not None:
            return True
    except Exception as e:
        return False

@register.filter
def event_in_cart(cart, event):
    #cart = Cart.objects.get(user=user)
    try:
        event = cart.events.get(id=event)
        if event is not None:
            return True
    except Exception as e:
        return False

@register.filter
def onedayclass_in_cart(cart, onedayclass):
    #cart = Cart.objects.get(user=user)
    try:
        onedayclass = cart.onedayclasses.get(id=onedayclass)
        if onedayclass is not None:
            return True
    except Exception as e:
        return False
