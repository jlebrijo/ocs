from django import template
from site_manager.models import Freebie, Quote
import datetime
register = template.Library()

@register.simple_tag
def freebie_of_day():
    f = Freebie.objects.filter(pub_date=datetime.date.today())[0]
    return f.link

@register.simple_tag
def quote_of_day():
    q = Quote.objects.filter(pub_date=datetime.date.today())[0]
    return q.text

@register.simple_tag
def encrypt(text):
    return text.replace('a','5').replace('b','6').replace('v','a').replace('w','b').replace('x','c')