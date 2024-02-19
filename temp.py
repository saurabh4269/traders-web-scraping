import requests
from bs4 import BeautifulSoup

def scrape_linkedin_profile(profile_url):
    response = requests.get(profile_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        name_element = soup.find('h1', class_='top-card-layout__title')
        name = name_element.text.strip() if name_element else 'Name Not Found'

        headline_element = soup.find('h2', class_='top-card-layout__headline')
        headline = headline_element.text.strip() if headline_element else 'Headline Not Found'

        location_element = soup.find('span', class_='top-card-layout__entity-info-value')
        location = location_element.text.strip() if location_element else 'Location Not Found'

        print(f"Name: {name}")
        print(f"Headline: {headline}")
        print(f"Location: {location}")
    else:
        print("Failed to retrieve LinkedIn profile. Status code:", response.status_code)

profile_url = 'https://www.linkedin.com/in/johndoe'
scrape_linkedin_profile(profile_url)
