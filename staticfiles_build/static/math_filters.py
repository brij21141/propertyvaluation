from django import template
import inflect  

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''

@register.filter
def divide(value, arg):
    try:
        return float(value) / float(arg) if float(arg) != 0 else ''
    except (ValueError, TypeError):
        return ''
@register.filter
def sum(value, arg):
    try:
        return float(value) + float(arg) 
    except (ValueError, TypeError):
        return ''
@register.simple_tag
def calculate_total(items):
    total = 0
    for item in items:
        total += item.bankid.internalrate 
    return total
@register.simple_tag
def calculate_gst(items):
    total = 0
    for item in items:
        total += item.bankid.internalrate *9/100
    return total
@register.simple_tag
def calculate_totalgst(items):
    total = 0
    for item in items:
        total += item.bankid.internalrate *9/100*2
    return total
@register.simple_tag
def calculate_grandtotal(items):
    total = 0
    for item in items:
        total += item.bankid.internalrate+item.bankid.internalrate *9/100*2
    return total

@register.simple_tag
def convert_amount_to_words(amount):  
    p = inflect.engine() 
    rswords = p.number_to_words(amount) 
    if amount == int(amount):
        # Remove "point zero" if present
        rswords = rswords.replace(" point zero", "")
    return  rswords

@register.simple_tag
def calculate_percent(itema, itemb):
    # total = 0
    # for item in items:
    print(itema  )
    total = itema *100/itemb
    return total