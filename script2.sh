#!/bin/bash

# Function to check country name by country code
check_country() {
    country_code="$1"
    api_url="https://www.travel-advisory.info/api"

    # Check if data.json file exists, if not, download data from the API
    if [ ! -f data.json ]; then
        echo "Fetching data from API..."
        curl -s "$api_url" > data.json
    fi

    # Use jq to parse JSON and extract country name
    country_name=$(jq -r --arg code "$country_code" '.data[$code].name' data.json)

    if [ "$country_name" == "null" ]; then
        echo "No such country found for $country_code."
    else
        echo "$country_code: $country_name"
    fi
}

# Function to process multiple country codes
process_multiple_codes() {
    for code in "$@"; do
        check_country "$code"
    done
}

# if no code passed
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 CODE"
    exit 1
fi

# process command line argument

while [ "$#" -gt 0 ]; do
    case "$1" in
        *)
            check_country "$1"
            ;;
    esac
    shift
done
