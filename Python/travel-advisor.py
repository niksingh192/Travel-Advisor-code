import requests
def check_country(country_code):
    api_url = "https://www.travel-advisory.info/api"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        country_name = data.get('data', {}).get(country_code, {}).get('name')
        
        if country_name:
            return f"{country_code}: {country_name}"
        else:
            return f"No such country found for {country_code}."
    else:
        return f"Error fetching data from the API. Status code: {response.status_code}"
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python check_country.py COUNTRY_CODE")
        sys.exit(1)
    
    country_code = sys.argv[1]
    result = check_country(country_code)
    print(result)
