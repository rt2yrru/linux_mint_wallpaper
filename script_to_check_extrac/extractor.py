import bs4
import httpx
from urllib.parse import urljoin

_parser = 'lxml'
_base_url = 'http://packages.linuxmint.com/pool/main/m/'

# Dictionary to hold our lists
results = {
    "artwork_deb": [],
    "backgrounds_deb": [],
    "wallpaper_deb": [],
    "artwork_tar_gz": [],
    "backgrounds_tar_gz": [],
    "wallpaper_tar_gz": []
}

keywords = ['artwork', 'backgrounds', 'wallpaper']

def scrape_mint_organized():
    with httpx.Client(follow_redirects=True, timeout=30.0) as client:
        print(f"Connecting to: {_base_url}")
        try:
            response = client.get(_base_url)
            response.raise_for_status()
        except Exception as e:
            print(f"Error: {e}")
            return

        soup = bs4.BeautifulSoup(response.text, _parser)
        
        # 1. Identify relevant sub-directories
        for link in soup.find_all('a'):
            href = link.get('href', '')
            folder_name = href.lower()
            
            # Determine which keyword matches the folder
            matched_key = next((key for key in keywords if key in folder_name), None)
            
            if matched_key:
                target_url = urljoin(_base_url, href)
                print(f"Scanning directory: {folder_name}")
                
                try:
                    res = client.get(target_url)
                    if res.status_code != 200: continue
                    
                    sub_soup = bs4.BeautifulSoup(res.text, _parser)
                    for file_link in sub_soup.find_all('a'):
                        file_href = file_link.get('href', '')
                        full_file_url = urljoin(target_url, file_href)
                        
                        # Sort into specific lists based on extension and keyword
                        if file_href.endswith('.deb'):
                            results[f"{matched_key}_deb"].append(full_file_url)
                        elif file_href.endswith('.tar.gz'):
                            results[f"{matched_key}_tar_gz"].append(full_file_url)
                            
                except Exception as e:
                    print(f"Error scanning {folder_name}: {e}")

    # 2. Save all lists to their respective files
    for key, urls in results.items():
        filename = f"{key}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for url in urls:
                f.write(f"{url}\n")
        print(f"Created {filename} with {len(urls)} links.")

if __name__ == "__main__":
    scrape_mint_organized()