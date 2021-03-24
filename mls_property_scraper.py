import requests
from bs4 import BeautifulSoup
import re

def scrape_property(url, pid, address):
    headers = {
        'accept': 
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    content = requests.get(url, headers=headers)
    soup = BeautifulSoup(content.text, "html.parser")

    def extract_el(label, parser=lambda x: x):
        try:
            el = soup.select_one(label)
            return '' if not el else parser(el.get_text())
        except Exception as e:
            return ''

    sell_date = extract_el('span.detail.salesclosedate')
    sell_price = extract_el('span.detail.soldprice', lambda x: '' if x == 'None' else re.sub(',', '', x[1:]))
    list_price = extract_el('span.detail.listprice', lambda x: '' if x == 'None' else re.sub(',', '', x[1:]))
    mls = extract_el('span.nmls', lambda x: x[5:]) # MLS ID
    address_long = address
    zip_code = extract_el('span.detail.postalcode')
    built = extract_el('span.detail.yearbuilt')
    city = extract_el('span.detail.city')
    county = extract_el('span.detail.county')
    property_type = extract_el('span.detail.property_type_display')
    num_bath = extract_el('span.detail.bathstotal')
    num_bed = extract_el('span.detail.bedrooms')
    fin_sqft = extract_el('span.detail.livingarea', lambda x: '' if x == 'None' else re.sub('[ ,]', '', x[0:-3]))
    above_gd_sqft = extract_el('span.detail.sqftaboveground', lambda x: '' if x == 'None' else re.sub('[ ,]', '', x[0:-3]))
    below_gd_sqft = extract_el('span.detail.sqftbelowground', lambda x: '' if x == 'None' else re.sub('[ ,]', '', x[0:-3]))
    appliances = extract_el('span.detail.appliances')
    num_fireplaces = extract_el('span.detail.fireplaces')
    basement_details = extract_el('span.detail.basement')
    common_wall = extract_el('span.detail.attached')
    heating = extract_el('span.detail.heatingdescription')
    ac = extract_el('span.detail.coolingdescription')
    amenities = extract_el('span.detail.amenitiesunit')
    ext_material = extract_el('span.detail.exterior')
    num_garage_spaces = extract_el('span.detail.parkinggarage')
    foundation_size = extract_el('span.detail.foundationsize', lambda x: '' if x == 'None' else re.sub('[ ,]', '', x[0:-3]))
    handicap = extract_el('span.detail.handicapaccess')
    out_buildings = extract_el('span.detail.outbuildings')
    pool = extract_el('span.detail.pooldescription')
    quarter_baths = extract_el('span.detail.bathquarter')
    half_baths = extract_el('span.detail.bathshalf')
    threequarter_baths = extract_el('span.detail.bathsthreequarter')
    full_baths = extract_el('span.detail.bathsfull')
    dining = extract_el('span.detail.diningroomdescription')
    family_room = extract_el('span.detail.roomfamilychar')
    lot = extract_el('span.detail.acres')
    lat = extract_el('span.detail.latitude')
    lng = extract_el('span.detail.longitude')
    zoning = extract_el('span.detail.zoning')
    school_district = extract_el('span.detail.schooldistrictnumber')
    association_fee = extract_el('span.detail.associationfee', lambda x: '' if x == 'None' else re.sub(',', '', x[1:]))
    tax_year = extract_el('span.detail.taxyear')
    annual_taxes = extract_el('span.detail.taxes', lambda x: '' if x == 'None' else re.sub(',', '', x[1:]))
    fuel = extract_el('span.detail.fuel')
    sewer = extract_el('span.detail.sewer')
    water = extract_el('span.detail.water')

    return {
        'pid': pid,
        'sell_date': sell_date,
        'sell_price': sell_price,
        'list_price': list_price,
        'mls': mls,
        'address_long': address_long,
        'zip_code': zip_code,
        'built': built,
        'city': city,
        'county': county,
        'property_type': property_type,
        'num_bath': num_bath,
        'num_bed': num_bed,
        'fin_sqft': fin_sqft,
        'above_gd_sqft': above_gd_sqft,
        'below_gd_sqft': below_gd_sqft,
        'appliances': appliances,
        'num_fireplaces': num_fireplaces,
        'basement_details': basement_details,
        'common_wall': common_wall,
        'heating': heating,
        'ac': ac,
        'amenities': amenities,
        'ext_material': ext_material,
        'num_garage_spaces': num_garage_spaces,
        'foundation_size': foundation_size,
        'handicap': handicap,
        'out_buildings': out_buildings,
        'pool': pool,
        'quarter_baths': quarter_baths,
        'half_baths': half_baths,
        'threequarter_baths': threequarter_baths,
        'full_baths': full_baths,
        'dining': dining,
        'family_room': family_room,
        'lot': lot,
        'lat': lat,
        'lng': lng,
        'zoning': zoning,
        'school_district': school_district,
        'association_fee': association_fee,
        'tax_year': tax_year,
        'annual_taxes': annual_taxes,
        'fuel': fuel,
        'sewer': sewer,
        'water': water
    }

def write_property_to_file(file, p):
    csv_line = ''
    for item in list(p.values()):
        csv_line = '%s,%s' % (csv_line, re.sub(",", ":", re.sub(' ', '',str(item))))
    csv_line = csv_line[1:]

    with open(file, 'a') as f:
        f.write(csv_line)
        f.write('\n')

####################################################
# Scrape
####################################################

import sys

if not (len(sys.argv) == 3):
    print('Need 2 arguments [input_dir] [output_dir]')
    sys.exit()

OUTPUT_FILE = sys.argv[2]
INPUT_FILE = sys.argv[1]

with open(OUTPUT_FILE, 'a') as f:
    f.write('pid,sell_date,sell_price,list_price,mls,address_long,zip_code,built,city,county,property_type,num_bath,num_bed,fin_sqft,above_gd_sqft,below_gd_sqft,appliances,num_fireplaces,basement_details,common_wall,heating,ac,amenities,ext_material,num_garage_spaces,foundation_size,handicap,out_buildings,pool,quarter_baths,half_baths,threequarter_baths,full_baths,dining,family_room,lot,lat,lng,zoning,school_district,association_fee,tax_year,annual_taxes,fuel,sewer,water')
    f.write('\n')

import pandas as pd

df_properties = pd.read_csv(INPUT_FILE, names=['pid','address'])
# df_properties = pd.read_csv('test.csv')

for (i, row) in df_properties.iterrows():
    [pid, address] = [row['pid'], row['address']]

    try:
        THE_MLS_PROPERTY_URL_FORMAT = 'https://www.themlsonline.com/minnesota-real-estate/listings/property/%d/%s'
        url = THE_MLS_PROPERTY_URL_FORMAT % (pid, address)
        print(url)

        # Initial scrape
        p = scrape_property(url, pid, address)
        if p:
            write_property_to_file(OUTPUT_FILE, p)
            print('[%-5d] %s...' % (i, str(p)[0:150]))

    except Exception as e:
        print('[%08d] %s' % (i, e))
