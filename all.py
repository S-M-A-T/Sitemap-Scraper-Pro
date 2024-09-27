import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to fetch URLs from the sitemap
def fetch_sitemap_urls(sitemap_url):
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the XML content with lxml parser
        soup = BeautifulSoup(response.content, 'lxml')  # Ensure 'lxml' is specified
        urls = [url.text for url in soup.find_all('loc')]
        
        return urls
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []

# Function to fetch all URLs across multiple pages
def fetch_all_sitemap_urls(base_url):
    all_urls = []
    page = 1
    while True:
        sitemap_url = f"{base_url}?page={page}"
        urls = fetch_sitemap_urls(sitemap_url)

        # Break the loop if no more URLs are found
        if not urls:
            break
        
        all_urls.extend(urls)
        print(f"Fetched {len(urls)} URLs from page {page}")
        page += 1

    return all_urls

# Function to scrape data from a single page
def scrape_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract Main category and Sub category
        breadcrumb = soup.find('nav', {'aria-label': 'breadcrumbs'})
        categories = breadcrumb.find_all('li') if breadcrumb else []
        main_category = categories[-2].text.strip() if len(categories) >= 2 else "Not Found"
        sub_category = categories[-1].text.strip() if categories else "Not Found"

        # Extract Title
        title = soup.find('h1', class_='my-3 text-2xl font-bold lg:text-3xl').text.strip()

        # Extract Country
        country = "United Arab Emirates"  # Hardcoded since it's constant for all entries

        # Extract Phone Number from the specific div structure
        phone_div = soup.find('div', class_='flex w-full items-center justify-center rounded-lg bg-cyan-50 p-4 text-center')
        if phone_div:
            phone_link = phone_div.find('a', href=True)
            phone_number = phone_link.text.strip() if phone_link else "Not Available"
        else:
            phone_number = "Not Available"

        return {
            "Main Category": main_category,
            "Sub Category": sub_category,
            "Title": title,
            "Country": country,
            "Phone Number": phone_number
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Base URL of the sitemap
base_url = "https://www.abcccc.com/sitemap.xml"

# Fetch all URLs from the sitemap
all_urls = fetch_all_sitemap_urls(base_url)

# Optional: Add specific URLs to your list if needed
urls = all_urls  # You can directly use the fetched URLs

# Loop through URLs and scrape data
scraped_data = []
for url in urls:
    data = scrape_data(url)
    if data:
        scraped_data.append(data)

# Save the scraped data to an Excel file
excel_file_path = "scraped_data.xlsx"
df = pd.DataFrame(scraped_data)
df.to_excel(excel_file_path, index=False)

# Print or save the scraped data
for entry in scraped_data:
    print(entry)

print(f"\nTotal data entries scraped: {len(scraped_data)}")
print(f"Data saved to {excel_file_path}")
