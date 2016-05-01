from django import template

from pin.models import Favorite

register = template.Library()


@register.filter
def is_favourited(bookmark, user):
    """
    {% if bookmark|is_favourited:request.user %}
        already favourited
    {% else %}
        not favourited yet
    {% endif %}
    """
    if not user.is_authenticated():
        return False
    return Favorite.objects.filter(bookmark=bookmark, user=user).exists()
