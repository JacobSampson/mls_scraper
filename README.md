# mls_scraper

Scrape all sold property data from The MLS Online: *[https://www.themlsonline.com/](https://www.themlsonline.com/minnesota-real-estate)*

---

| <a href="https://sampsonjacob.com" target="_blank">**Jacob Sampson**</a> |
| :----------------------------------------------------------: |
| [![JacobSampson](https://avatars3.githubusercontent.com/u/42616056?s=200&v=4)](http://sampsonjacob.com) |
| <a href="http://linkedin.com/in/jacob-i-sampson" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> <a href="mailto: jacob.samps@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>  |

## Data

Collected data is in the `output` directory as `properties.csv`. There are 102,956 properties listed with their sell date, sell price, and listing price along with house attributes.

### Fields

| Column | Description | Type | 
| :----------------------------------------------------------: |
| pid |  | `string` |
| sell_date |  | `string` |
| sell_price |  | `string` |
| list_price |  | `string` |
| mls |  | `string` |
| address_long |  | `string` |
| zip_code |  | `string` |
| built | | `string` |
| city | | `string` |
| county | | `string` |
| property_type | | `string` |
| num_bath | | `string` |
| num_bed | | `string` |
| fin_sqft | | `string` |
| above_gd_sqft | | `string` |
| below_gd_sqft | | `string` |
| appliances | | `string` |
| num_fireplaces | | `string` |
| basement_details | | `string` |
| common_wall | | `string` |
| heating | | `string` |
| ac | | `string` |
| amenities | | `string` |
| ext_material | | `string` |
| num_garage_spaces | | `string` |
| foundation_size | | `string` |
| handicap | | `string` |
| out_buildings | | `string` |
| pool | | `string` |
| quarter_baths | | `string` |
| half_baths | | `string` |
| threequarter_baths | | `string` |
| full_baths | | `string` |
| dining | | `string` |
| family_room | | `string` |
| lot | | `string` |
| lat | | `string` |
| lng | | `string` |
| zoning | | `string` |
| school_district | | `string` |
| association_fee | | `string` |
| tax_year | | `string` |
| annual_taxes | | `string` |
| fuel | | `string` |
| sewer | | `string` |
| water | | `string` |




## How to Use

`run.sh` and `combine.sh` are helper scripts for running the two Python scripts. The scraping is down with BeautifulSoupt4.

### Files


`mls_listings_scraper.py` scrapes all listings from the site with the 'Sold' tag (output as `listings.csv`) 

`mls_property_scraper.py` scrapes properties given the property ID and address scraped from the listings (output as `properties.csv`)
