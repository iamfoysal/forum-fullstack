from django import template
  
register = template.Library()
  

@register.filter()
def rezise(value):
    return value [:150]+"......"

# register.filter('ragne_filters', ragne_filters)