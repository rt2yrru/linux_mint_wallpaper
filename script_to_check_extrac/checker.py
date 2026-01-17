import httpx
import os
import sys

# ANSI Color Codes
class Color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    VIOLET = '\033[95m'
    END = '\033[0m'
    BOLD = '\033[1m'

FILE_LISTS = [
    "artwork_deb.txt", "backgrounds_deb.txt", "wallpaper_deb.txt",
    "artwork_tar_gz.txt", "backgrounds_tar_gz.txt", "wallpaper_tar_gz.txt"
]

LIMIT_MB = 2
LIMIT_BYTES = LIMIT_MB * 1024 * 1024
ERROR_FILE = "error.txt"

def test_link(client, url):
    """Downloads up to 2MB in memory to verify the link."""
    try:
        # Print blue while testing
        sys.stdout.write(f"{Color.BLUE}[TESTING]{Color.END} {url}\r")
        sys.stdout.flush()
        
        with client.stream("GET", url) as response:
            if response.status_code != 200:
                return False, f"HTTP {response.status_code}"
            
            bytes_received = 0
            for chunk in response.iter_bytes(chunk_size=8192):
                bytes_received += len(chunk)
                if bytes_received >= LIMIT_BYTES:
                    break
            return True, "Verified"
    except Exception as e:
        return False, str(e)

def process_and_clean():
    # Ensure error.txt starts fresh or exists
    with open(ERROR_FILE, "a") as f: pass 

    with httpx.Client(follow_redirects=True, timeout=15.0) as client:
        for file_name in FILE_LISTS:
            if not os.path.exists(file_name):
                continue
            
            print(f"\n{Color.BOLD}Checking File: {file_name}{Color.END}")
            
            with open(file_name, "r") as f:
                links = [line.strip() for line in f if line.strip()]
            
            # Print all links as Violet (Awaiting) first
            for url in links:
                print(f"{Color.VIOLET}[AWAITING]{Color.END} {url}")

            valid_links = []
            failed_links = []

            # Move cursor back up to start testing (standard terminal simulation)
            print(f"\n--- Starting Validation ---")

            for url in links:
                success, message = test_link(client, url)
                
                # Clear the line and print final status
                sys.stdout.write("\033[K") # Clear line
                if success:
                    print(f"{Color.GREEN}[PASSED]{Color.END} {url}")
                    valid_links.append(url)
                else:
                    print(f"{Color.RED}[FAILED]{Color.END} {url} - {message}")
                    failed_links.append(f"{url} | Error: {message}")

            # Save failed links
            if failed_links:
                with open(ERROR_FILE, "a") as ef:
                    for entry in failed_links:
                        ef.write(f"{entry}\n")

            # Overwrite original file
            with open(file_name, "w") as f:
                for link in valid_links:
                    f.write(f"{link}\n")
            
            print(f"{Color.BOLD}Summary for {file_name}: {len(valid_links)} kept, {len(failed_links)} removed.{Color.END}")

if __name__ == "__main__":
    # Check if the terminal supports colors (Windows needs help sometimes)
    if os.name == 'nt':
        os.system('color')
        
    process_and_clean()