#!/bin/bash

curl -s https://www.amfiindia.com/spages/NAVAll.txt |
awk -F ';' 'BEGIN { OFS="\t" }
NR>1 && NF>=5 { print $4, $5 }' > amfi_schemes.tsv

echo "Saved to amfi_schemes.tsv"
