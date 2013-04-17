from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def direction_name(direction):
    d = direction.upper()
    if d == 'N':
        return 'North'
    if d == 'S':
        return 'South'
    if d == 'E':
        return 'East'
    if d == 'W':
        return 'West'