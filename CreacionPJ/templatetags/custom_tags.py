from django import template

register = template.Library()

@register.filter
def exists_in_dictionary(value, dictionary):
  return value in dictionary

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)