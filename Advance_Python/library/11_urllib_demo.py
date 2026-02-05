import urllib.request
import urllib.parse

"""
Python urllib Module
A package that collects several modules for working with URLs.
"""

# 1. Opening a URL (urllib.request)
try:
    print("--- Fetching data from python.org ---")
    with urllib.request.urlopen("https://www.python.org") as response:
        html = response.read()
        print(f"Response Status: {response.status}")
        print(f"Response Headers: {response.getheader('Content-Type')}")
        print(f"Content Length: {len(html)} bytes")
        # print(html[:200]) # Print first 200 chars
except Exception as e:
    print(f"Error fetching URL: {e}")

# 2. Parsing and Building URLs (urllib.parse)
url = "https://www.google.com/search?q=python+library&hl=en"
parsed_url = urllib.parse.urlparse(url)
print("\n--- Parsed URL ---")
print(f"Scheme: {parsed_url.scheme}")
print(f"Netloc: {parsed_url.netloc}")
print(f"Path: {parsed_url.path}")
print(f"Query: {parsed_url.query}")

# 3. Building Query Strings
params = {'name': 'Alice', 'role': 'Admin', 'city': 'San Francisco'}
query_string = urllib.parse.urlencode(params)
print(f"\nEncoded Query: {query_string}")

full_url = "https://api.example.com/user?" + query_string
print(f"Full URL: {full_url}")

# 4. Parsing Query Strings
parsed_params = urllib.parse.parse_qs(query_string)
print(f"Parsed Params: {parsed_params}")
