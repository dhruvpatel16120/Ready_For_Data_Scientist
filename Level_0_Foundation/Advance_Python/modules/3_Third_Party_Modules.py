"""
To use third-party modules, you typically install them via pip:
pip install requests
"""

import requests

print("--- Third-Party Module Demo (requests) ---")

# Making a GET request to a public API (GitHub API)
response = requests.get('https://api.github.com/zen')
    
if response.status_code == 200:
    print("Successfully connected to GitHub API!")
    print(f"Random Zen Quote: {response.text}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
