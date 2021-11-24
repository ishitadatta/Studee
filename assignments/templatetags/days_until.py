from datetime import datetime
from django import template

register = template.Library()


@register.filter
def days_until(date):
    delta = datetime.date(date) - datetime.now().date()
    return delta.days