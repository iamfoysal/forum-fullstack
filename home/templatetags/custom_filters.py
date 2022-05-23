from django import template

register = template.Library()


@register.filter("text_filters")
def text_filters(value):
    return value [0:150] + "......"

# register.filter('ragne_filters', ragne_filters)