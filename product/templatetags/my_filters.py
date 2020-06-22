from django import template


import re
register = template.Library()
register2 = template.Library()

@register.filter(name='times') 
def times(number):
    return range(1,number+1)

@register.filter(name='replace_prev')
def replace_prev(url):
    page_number = 0
    pattern = re.compile(r'\d$')
    if url:
        page_number = int(pattern.search(url).group())
    
    if  page_number > 1:
         page_number -= 1
            
    
    new_page = str(page_number)

    return re.sub(r'\d$',new_page,url)

@register.filter(name='replace_next')
def replace_next(url,number_of_pages = 0):
    page_number = 0
    pattern = re.compile(r'\d$')
    if url:
        page_number = int(pattern.search(url).group())

    if page_number < number_of_pages:
        page_number += 1


    new_page = str(page_number)

    return re.sub(r'\d$',new_page,url)

