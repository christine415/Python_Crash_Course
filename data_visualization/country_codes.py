from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    if country_name == 'Yemen, Rep.':
        return 'ye'
    return None

#print(get_country_code('Andorra'))
#print(get_country_code('United Arab Emirates'))