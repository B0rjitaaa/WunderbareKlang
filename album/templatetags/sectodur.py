# Import template library
from django import template

# Set register
register = template.Library()

# Register filter
@register.filter
def sectodur(ms, arg = 'short'):
    s=int(ms)/1000 
    m,s=divmod(s,60) 
    h,m=divmod(m,60) 
    d,h=divmod(h,24)

    s = str(int(s))
    m = str(int(m))
    
    if int(s) < 10:
        s = '0' + s
    elif int(m) < 10:
        m = '0' + m
    duration = m + ':' + s
    return duration