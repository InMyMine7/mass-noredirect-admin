import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
import time
from colorama import Fore, init, Style

init(autoreset=True)
g = Fore.GREEN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
wh = Fore.WHITE + Style.BRIGHT

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

def check_url(base_url, path):
    elapsed_time = 0  
    try:
        if not base_url.endswith('/'):
            base_url += '/'
        full_url = urllib.parse.urljoin(base_url, path)
        start_time = time.time()
        response = requests.get(full_url, allow_redirects=False, timeout=5)
        elapsed_time = time.time() - start_time
        if response.status_code == 200:
            content = response.text.lower()
            dashboard_keywords = ['dashboard', 'admin', 'control panel', 'overview', 'home', 'Gallery']
            if any(keyword in content for keyword in dashboard_keywords):
                return f"{wh}[{g}VULNERABLE{wh}] {full_url} - Status: {response.status_code} - Likely dashboard (Time: {elapsed_time:.2f}s)"
            else:
                return f"{wh}[{y}CHECK MANUAL{wh}] {full_url} - Status: {response.status_code} - No dashboard keywords (Time: {elapsed_time:.2f}s)"
        elif response.status_code in [301, 302, 303, 307, 308]:
            return f"[REDIRECT] {full_url} - Status: {response.status_code} - Redirects to {response.headers.get('Location', 'unknown')} (Time: {elapsed_time:.2f}s)"
        else:
            return f"[NOT VULNERABLE] {full_url} - Status: {response.status_code} (Time: {elapsed_time:.2f}s)"
    except requests.exceptions.RequestException as e:
        return f"[ERROR] {full_url} - Failed to connect: (Time: {elapsed_time:.2f}s)"

def main():
    print(f"{g}github.com/InMyMine7")
    url_file = input("Enter the name of the URL file you want to scan (eg: list.txt): ").strip()
    path_file = 'path.txt'

    paths = read_file(path_file)
    if not paths:
        print("No paths found in path.txt. Exiting.")
        return

    urls = read_file(url_file)
    if not urls:
        print(f"No URLs found in {url_file}. Exiting.")
        return

    print("\nChecking URLs for admin dashboard access...\n")
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls:
            futures = [executor.submit(check_url, url, path) for path in paths]
            for future in futures:
                print(future.result())

if __name__ == "__main__":
    main()
