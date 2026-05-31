# Exercise 51: URL Shortener
# Objective: URLShortener class using hashlib for 6-char hash codes

import hashlib

class URLShortener:
    def __init__(self):
        self._store = {}

    def shorten(self, url):
        if not url.startswith(("http://", "https://")):
            raise ValueError("URL must start with http:// or https://")
        code = hashlib.md5(url.encode()).hexdigest()[:6]
        self._store[code] = url
        return code

    def redirect(self, code):
        if code not in self._store:
            print(f"Error: Short code '{code}' not found.")
            return None
        return self._store[code]

    def display(self):
        print(f"{'Code':<8} -> URL")
        print("-" * 55)
        for code, url in self._store.items():
            print(f"{code:<8} -> {url}")

shortener = URLShortener()
urls = ["https://www.google.com",
        "https://github.com/cognizant/training",
        "https://docs.python.org/3/"]

for url in urls:
    code = shortener.shorten(url)
    print(f"Shortened: {url}  ->  {code}")

print()
shortener.display()
print()
code     = shortener.shorten(urls[0])
original = shortener.redirect(code)
print(f"Redirect '{code}' -> {original}")
