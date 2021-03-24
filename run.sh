# ./run.sh ./input 10000 ./output

sed '1d' $1/listings.csv > $1/trimmed_listings.csv

# split [file] -l [lines]
split $1/trimmed_listings.csv -l $2 $1/

echo "Scraping..."
for i in $(ls $1); do
    if ! [[ ($i =~ .*.csv) ]];
    then echo "python mls_property_scraper.py $1/$i $3/properties_$i.csv"; python mls_property_scraper.py $1/$i $3/properties_$i.csv &
    fi
done

rm $1/trimmed_listings.csv
