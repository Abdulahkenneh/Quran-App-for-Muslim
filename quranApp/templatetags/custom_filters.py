from django import template

register = template.Library()

@register.filter
def zip_lists(list1, list2,list3):
    return zip(list1, list2,list3)

@register.filter
def remove_last_n_characters(value, n):
    """Returns the last n characters of the input string."""
    if isinstance(value, str) and isinstance(n, int):
        return value[:-n]
    return value  # Y