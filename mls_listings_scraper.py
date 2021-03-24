import requests
from bs4 import BeautifulSoup

def scrape_listings(url):
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

    property_urls = [a['href'] for a in soup.find_all("a", {"class": "photo-count"})]

    next_url = None
    next_href = soup.select_one('a.next.btn.btn-default')
    if next_href and (not soup.select_one('a.next.btn.btn-default.disabled')):
      next_url = next_href['href']

    return [next_url, property_urls]

def write_listings_to_file(file, listings):
    listings = '\n'.join(['%d,%s' % (int(url.split('/')[-2]), url.split('/')[-1]) for url in listings])
    with open(file, 'a') as f:
        f.write(listings)
        f.write('\n')

####################################################
# Scrape
####################################################

OUTPUT_FILE = './output/listings.csv'

with open(OUTPUT_FILE, 'a') as f:
    f.write('pid,address')
    f.write('\n')
    # From here, can go to https://www.themlsonline.com/minnesota-real-estate/listings/property/{pid}/{address}

i = 0
try:
    THE_MLS_ONLINE_URL_FORMAT = 'https://www.themlsonline.com/minnesota-real-estate/search/results/ac11655f4574704918af0985873eb64'

    # Initial scrape
    [next_url, listings] = scrape_listings(THE_MLS_ONLINE_URL_FORMAT)
    if listings:
            write_listings_to_file(OUTPUT_FILE, listings)
            print('[%-5d] %s...' % (i, str(listings)[0:150]))

    # Continue scraping if 'next' has a valid references
    while next_url:
        [next_url, listings] = scrape_listings(next_url)
        if listings:
            write_listings_to_file(OUTPUT_FILE, listings)
            print('[%-5d] %s...' % (i, str(listings)[0:150]))
        i += 1
except Exception as e:
    print('[%08d] %s' % (i, e))
