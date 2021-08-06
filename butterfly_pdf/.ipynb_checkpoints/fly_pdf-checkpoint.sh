#!/bin/bash

# This script gets initial data from the character counts of lines in animal_data.txt
# It uses these numbers as input to python which outputs plots
# The plots are added to a web page (html) and PDF document

# Initial parameters

rho="28"
beta="2.67"

# remove file if it already exists
rm initdata.txt

# get unique character counts of animal_data.txt lines
for i in `cat animal_data.txt`; do echo $i | wc -m >> initdata.txt; done
mynums=`cat initdata.txt | sort | uniq`

# make plots
for i in $mynums
do
	python butterfly.py $i $rho $beta
	echo "made plot for sigma = $i"
done

# generate html file that contains all generated plots
echo "
<!DOCTYPE html>
<html>
<body>
" > myimages.html

for i in fig*
do
	echo "
	<h2>$i</h2>
	<img src=\"$i\" alt=\"$i\" width=\"500\" height=\"300\">
	" >> myimages.html
done

echo "
</body>
</html>
" >> myimages.html

# convert html page to PDF
pandoc myimages.html -o myimages.pdf