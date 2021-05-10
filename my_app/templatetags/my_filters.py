from django import template

register = template.Library()

# custom filtering templates by adding extra str
def my_filter(value):
    return value + " like a boss"

# custom filtering templates by adding extra arg
def my_filter2(value, arg):
    return value + " " + arg


register.filter('custom_filter', my_filter )
register.filter('custom_filter2', my_filter2 )
