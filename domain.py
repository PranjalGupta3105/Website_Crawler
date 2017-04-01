from urllib.parse import urlparse


#Getting the Domain Name
def get_domain_name(url):
    try:
        results=get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''



#Getting the Sub domain
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


