# Subdomain Enumerator

A  Python program that enumerates subdomains against a SecList wordlist.

## Features
- Supports both `http` and `https` protocols.
- Rate-limiting handling.
- Multithreading for faster enumeration.

## Installation
1. Clone the repository:
    ```bash
    git clone git clone https://github.com/0xWiIIiam/subdomain-enumerator.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your custom wordlist in `list.txt` or just use the current one.

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
