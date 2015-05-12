import os
import random
import string
import uuid
import urllib2

from django.conf import settings
from django.contrib.gis.geoip import GeoIP
from actors import globals
# from system.models import Setting
# from system.models import IpBlocking

def days_between_dates(d1, d2):
    d = d2-d1
    return d.days

def make_uuid():
    return str(uuid.uuid4().hex)

def calculateCommision(price, quantity, fixido_percentage):
    return ((fixido_percentage/100 * price) * quantity) 

def getExternalIP():
    return urllib2.urlopen('http://automation.whatismyip.com/n09230945.asp').read()

def generatePassword():
    """ Generate random password
    """
    random.seed = (os.urandom(1024))
    pwd = random.choice(string.ascii_lowercase)
    pwd += random.choice(string.ascii_lowercase)
    return '%s%04d' % (pwd, random.randrange(1, 9999))

def get_global_language(request):
    """ This function get global language based on following assets
        
        1. authenticated user's language
        2. cookie
        2. fixido select language
        3. query string
        4. brower setting
        5. default sweden
    """
    cookies_language = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)
    if cookies_language:
        select_language = request.POST.get('language', None)
        
        if select_language and select_language != cookies_language:
            cookies_language = select_language
    else:
       url_language = request.GET.get('la', request.POST.get('language', '')).strip()
       if url_language and url_language.lower() != 'none':
            cookies_language = url_language
       else:
            try:
                user_ip = globals.ip
                if user_ip.startswith('127.0.0'):
                    user_ip = '106.51.234.149'
                g = GeoIP()
                country = g.country_code(user_ip)
                language_list = ['en','sv','de']
                country_language_dict = {
                    'AU':'en','IN':'en','SE':'sv','DE':'de',
                    'US':'en','GB':'en','CA':'en','AF':'aa','AX':'en',
                    'AL':'sq','DZ':'ar','AS':'en','AD':'ca','AO':'pt',
                    'AI':'en','AQ':'en','AG':'en','AR':'es','AM':'en',
                    'AW':'nl','AT':'de','AZ':'az','BS':'en','BH':'en',
                    'BD':'en','BB':'en','BY':'en','BE':'fr','BZ':'en',
                    'BM':'en','BT':'en','BO':'es','BQ':'es','BA':'bs',
                    'BW':'en','BV':'en','BR':'pt','IO':'en','BN':'en',
                    'BG':'en','BF':'en','BI':'en','KH':'km','CM':'fr',
                    'CA':'en','CV':'pt','KY':'en','CF':'fr','TD':'fr',
                    'CL':'es','CN':'zh','CX':'en','CC':'en','CO':'es',
                    'KM':'es','CG':'fr','CD':'fr','CK':'en','CR':'es',
                    'CI':'en','HR':'hr','CU':'es','CW':'fr','CY':'el',
                    'CZ':'cs','DK':'da','DJ':'en','DM':'en','DO':'es',
                    'EC':'es','EG':'ar','SV':'es','GQ':'fr','ER':'en',
                    'EE':'et','ET':'am','FK':'en','FO':'da','FJ':'en',
                    'FI':'sv','FR':'fr','GF':'fr','PF':'fr','TF':'fr',
                    'GA':'fr','GM':'en','GE':'en','DE':'de','GH':'en',
                    'GI':'en','GR':'el','GL':'kl','GD':'en','GP':'fr',
                    'GU':'en','GT':'es','GG':'fr','GN':'fr','GW':'fr',
                    'GY':'en','HT':'fr','HM':'en','VA':'en','HN':'es',
                    'HK':'en','HU':'hu','IS':'en','ID':'id','IR':'fa',
                    'IQ':'ar','IE':'en','IM':'en','IL':'ar','IT':'it',
                    'JM':'en','JP':'ja','JE':'en','JO':'ar','KZ':'ru',
                    'KE':'sw','KI':'en','KP':'ko','KR':'ko','KW':'ar',
                    'KG':'ru','LA':'lo','LV':'lv','LB':'ar','LS':'en',
                    'LR':'li','LY':'ar','LI':'de','LT':'lt','LU':'de',
                    'MO':'pt','MK':'mk','MG':'fr','MW':'en','MY':'ms',
                    'MV':'en','ML':'fr','MT':'fr','MH':'en','MQ':'fr',
                    'MR':'ar','MU':'en','YT':'fr','MX':'es','FM':'en',
                    'MD':'en','MC':'fr','MN':'mn','ME':'en','MS':'en',
                    'MA':'fr','MZ':'pt','MM':'my','NA':'en','NR':'en',
                    'NP':'ne','NL':'nl','NC':'en','NZ':'en','NI':'es',
                    'NE':'fr','NG':'en','NU':'en','NF':'en','MP':'en',
                    'NO':'no','OM':'ar','PK':'ur','PW':'en','PS':'ar',
                    'PA':'es','PG':'en','PY':'es','PE':'es','PH':'en',
                    'PN':'en','PL':'pl','PT':'pt','PR':'es','QA':'ar',
                    'RE':'ro','RO':'ro','RU':'ru','RW':'fr','BL':'en',
                    'SK':'en','KN':'en','LC':'en','MF':'en','PM':'en',
                    'WS':'en','SM':'it','ST':'pt','SA':'ar','SN':'fr',
                    'RS':'sr','SC':'fr','SL':'en','SG':'en','SX':'en',
                    'SK':'sk','SI':'sl','SB':'en','SO':'ar','ZA':'en',
                    'GS':'en','SS':'su','ES':'es','LK':'en','SD':'su',
                    'SR':'nl','SJ':'en','SZ':'en','SE':'sv','CH':'de',
                    'SY':'ar','TW':'en','TJ':'fa','TZ':'en','TH':'th',
                    'TL':'pt','TG':'fr','TK':'en','TO':'en','TT':'en',
                    'TN':'ar','TR':'tr','TM':'tk','TC':'en','TV':'en',
                    'UG':'en','UA':'uk','AE':'ar','GB':'en','US':'en',
                    'UM':'en','UY':'es','UZ':'uz','VU':'fr','VE':'ve',
                    'VN':'vi','VG':'en','VI':'en','WF':'fr','EH':'ar',
                    'YE':'ar','ZM':'en','ZW':'en',}
                if country_language_dict[country] in language_list:
                    return country_language_dict[country]
                else:
                    selected_language = 'en'
                    return selected_language
            except Exception as e:
                cookies_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'sv').split(',')[0]
    return cookies_language[:2]

def format_redirect_url(redirect_path, query_string):
    ''' utility to format redirect url with fixido query string
    '''
    stop_popup = True if 'st=' in query_string else False
    
    url_join_str = '?'
    if url_join_str in redirect_path:
        redirect_path, qs = redirect_path.split(url_join_str, 1)
        query_string = qs + '&' + query_string
    
    qs = {}
    for q in query_string.split('&'):
        if '=' in q:
            k, v = q.split('=', 1)
            qs[k] = v
    
    if stop_popup:
        if qs.has_key('zr'): del qs['zr']
        if qs.has_key('lr'): del qs['lr']
        if qs.has_key('ler'): del qs['ler']
        if qs.has_key('thanks'): del qs['thanks']
    
    query_string = ''
    for k in qs:
        query_string += k + '=' + qs[k] + '&'
        
    return redirect_path + url_join_str + query_string[:-1]

def get_user_from_session_key(session_key):
    ''' This utility fetches user from session user
    '''
    from django.utils.importlib import import_module
    from django.contrib.auth import get_user
    from django.contrib.auth.models import AnonymousUser
    from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, load_backend

    engine = import_module(settings.SESSION_ENGINE)
    session = engine.SessionStore(session_key)

    try:
        user_id = session[SESSION_KEY]
        backend_path = session[BACKEND_SESSION_KEY]
        backend = load_backend(backend_path)
        user = backend.get_user(user_id) or AnonymousUser()
    except KeyError:
        user = AnonymousUser()

    return user

def remove_none(field, empty_str=''):
    ''' This utility remove none and select strings
    '''
    try:
        if not field or field.lower() == 'none' or field.lower() == 'select':
            return empty_str
    except Exception, e:
        pass
    return field

def get_global_ip(request):
    ''' This utility gets client's IP address from the request
    '''
    return request.META.get('HTTP_X_FORWARDED_FOR', 
            request.META.get('REMOTE_ADDR', '127.0.0.1'))

def check_moderation():
    return Setting.objects.filter(parameter_name='moderation', 
                                  parameter_value='true').exists()

def get_days(unit):
    ''' converts unit of date to number of days
    >>> get_days('weeks')
    >>> 7
    >>> get_days('minutes')
    >>> 0
    '''
    days = { 
        'day': 1, 'week': 7,
        'month': 30, 'year': 365,
    }
    return days[unit] if days.has_key(unit) else 0

def get_only_value(val, default=None):
    if val:
        return val
    else:
        return default

def ip_checking(ip_val):
    fixido_ip_blocking = IpBlocking.objects.filter()
    for ip in fixido_ip_blocking:
        if ip.ip_type == "SI":
            if ip_val == ip.from_value:
                return True
        elif ip.ip_type == "SW":
            if ip_val.startswith(ip.from_value):
                return True
        elif ip.ip_type == "EW":
            if ip_val.endswith(ip.from_value):
                return True
        elif ip.ip_type == "RA":
            check_ip_val        = (ip_val).split('.')
            check_ip_val_length = len(check_ip_val)
            last_check_ip_val   = int(check_ip_val[check_ip_val_length-1])

            from_val            = (ip.from_value).split('.')
            from_val_length     = len(from_val)
            last_from_val       = int(from_val[from_val_length-1])

            to_val              = (ip.to_value).split('.')
            to_val_length       = len(to_val)
            last_to_val         = int(to_val[to_val_length-1])
            
            if check_ip_val[:check_ip_val_length-1] == from_val[:from_val_length-1]:
                block_ip_list = list(range(int(last_from_val),int(last_to_val)+1))
                if last_check_ip_val in block_ip_list:
                    return True
    return False