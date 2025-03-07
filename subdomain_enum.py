import requests
import concurrent.futures
import os
import sys
import time

WORDLIST_PATH = "list.txt"

# user-agent to prevent certain websites blocking our requests
HEADERS = {
    "User-Agent": "SubdomainEnumerator"
}

# loads the subdomains from the list.txt and returns a list of subdomains from the wordlist
def load_subdomains():
    if not os.path.exists(WORDLIST_PATH):
        exit()
    with open(WORDLIST_PATH, "r") as file:
        return [line.strip() for line in file]

# checks if a subdomain exists by sending a get request
def check_subdomain(subdomain, domain, index, total_subdomains):
    urls = [f"https://{subdomain}.{domain}", f"http://{subdomain}.{domain}"]
    
    for url in urls:
        try:
            response = requests.get(url, headers=HEADERS, timeout=3)
            if response.status_code < 400:
                print(f"[+] Found: {url}")
                break  
        except requests.RequestException:
            pass
    
    progress = (index + 1) / total_subdomains * 100
    sys.stdout.write(f"\rProgress: {progress:.1f}%")
    sys.stdout.flush()

    time.sleep(0.5)

# enumerates through the list of subdomains using multithreating to check multiple subdomains in parallel
def enumerate_subdomains(domain):
    subdomains = load_subdomains()
    total_subdomains = len(subdomains)

    print("Running subdomain enumeration...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for index, subdomain in enumerate(subdomains):
            futures.append(executor.submit(check_subdomain, subdomain, domain, index, total_subdomains))

        concurrent.futures.wait(futures)

    print("\nEnumeration complete!")

if __name__ == "__main__":
    target_domain = input("Enter domain (e.g., google.com): ")
    enumerate_subdomains(target_domain)
