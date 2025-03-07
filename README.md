# Subdomain Enumerator

A  Python program that enumerates subdomains against a SecLists wordlist.

## Features
- Supports both `http` and `https` protocols.
- Rate-limiting handling.
- Multithreading for faster enumeration.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/subdomain-enumerator.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your custom wordlist in `list.txt`.

4. Run the script:
    ```bash
    python subdomain_enum.py
    ```

## Example
```bash
Enter domain (e.g., google.com): example.com
Running subdomain enumeration...
Progress: 50.5%
[+] Found: http://www.example.com
