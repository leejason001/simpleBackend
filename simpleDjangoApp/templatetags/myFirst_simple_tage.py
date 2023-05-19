from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag
def myFirst_simple_tag(aTeacher):
    return aTeacher.cls.all()