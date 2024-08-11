def get_product_name(container):
    try:
        x = container.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text
    except:
        x = None
    return x

def get_product_rating(container):
    try:
        x = container.find('span', {'class': 'a-icon-alt'}).text.replace(' من 5 نجوم', '')
    except:
        x = None
    return x

def get_product_nreviews(container):
    try:
        x = container.find('span', {'class': 'a-size-base s-underline-text'}).text.replace(',', '')
    except:
        x = None
    return x

def get_product_price(container):
    try:
        x = container.find('span', {'class': 'a-offscreen'}).text.replace(',', '').replace('\u200f', '').replace('\xa0جنيه', '')
    except:
        x = None
    return x
