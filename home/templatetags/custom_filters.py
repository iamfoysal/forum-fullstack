from django import template

register = template.Library()


# @register.filter()
def ragne_filters(value):
    return value [0:150] + "......"

register.filter('ragne_filters', ragne_filters)