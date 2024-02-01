from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active(context, view_name, *args, **kwargs):
    request = context['request']

    try:
        url = reverse(view_name, args=args, kwargs=kwargs)
    except NoReverseMatch:
        url = ''

    if request.path == url:
        return 'active'
    return ''
