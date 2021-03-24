output_files=$(ls $1)

cd $1

echo "Combining files..."
cat $output_files > properties.csv
