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

*The following are my best interpretations of the field types and units from gathered listings*

| Column | Description | Type | Units |
| :--------------------------- |:----------------------------------------------------------|:----------------------------------------------------------:| :---: |
| pid | Unique ID for property listing | `string` | |
| sell_date | Sale closing date | `date` | |
| sell_price | Sale price | `int` | $ |
| list_price | Listed price | `int` | $ |
| mls | NMLS# (Nationwide Multistate Licensing System & Registry) | `int` | |
| address_long | Address | `string` | |
| zip_code | Zip code | `int` | |
| built | Year built | `int` | |
| city | City | `string` | |
| county | County | `string` | |
| property_type | Property type | `string` | enum |
| num_bath | Number of baths | `int` | |
| num_bed | Number of bedrooms | `int` | |
| fin_sqft | Finished / Living area | `int`  | sq ft |
| above_gd_sqft | Above ground living | `int` | sq ft |
| below_gd_sqft | Below ground living | `int` | sq ft |
| appliances | Included appliances | `string` | list |
| num_fireplaces | Number of fireplaces | `int` | |
| basement_details | Details about basement (setup, flooring...) | `string` | list |
| common_wall | Has a common wall | `bool` | |
| heating | Type of heating (forced air...) | `string` | enum |
| ac | Type of air conditioning | `string` | enum |
| amenities | General included amenities (e.g. hardwood floors, washer/dryer) | `string` | list |
| ext_material | Exterior material | `string` | enum |
| num_garage_spaces | Number of spaces in garage(s) | `int` | |
| foundation_size | Size of foundation | `int` | sq ft |
| handicap | Handicap accessible options and limitations | `string` | list |
| out_buildings | Outdoor buildings (sheds...) | `string` | list |
| pool | Descriptions of any pools | `string` | list |
| quarter_baths | Number of quarter baths | `int` | |
| half_baths | Number of half baths | `int` | |
| threequarter_baths | Number of three quarter baths | `int` | |
| full_baths | Number of full baths | `int` | |
| dining | Type of dining | `string` | enum/list |
| family_room | Location of family room | `string` | enum |
| lot | Acres | `float` | |
| lat | Latitude | `float` | |
| lng | Longitude | `float` | |
| zoning | Zoning type of property | `string` | enum |
| school_district | School district number | `int` | |
| association_fee | Fees for any property associations | `int` | $ |
| tax_year | Tax year assessment | `int` | |
| annual_taxes | Annual taxes | `int` | $ |
| fuel | Fuel system | `string` | enum |
| sewer | Sewer system | `string` | enum |
| water | Water system | `string` | enum |

## How to Use

`run.sh` and `combine.sh` are helper scripts for running the two Python scripts. The scraping is down with BeautifulSoupt4.

### Files


`mls_listings_scraper.py` scrapes all listings from the site with the 'Sold' tag (output as `listings.csv`) 

`mls_property_scraper.py` scrapes properties given the property ID and address scraped from the listings (output as `properties.csv`)
