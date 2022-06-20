from django import template

register = template.Library()


@register.filter()
def remainder(n):
    return n % 3

@register.filter(name='format')
def format(value, fmt):
    return fmt.format(value)