import json
import random
import string

FILE_NAME = "urls.json"

def load_urls():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_urls(urls):
    with open(FILE_NAME, "w") as file:
        json.dump(urls, file, indent=4)

def shorten_url(long_url):
    urls = load_urls()
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    urls[short_code] = long_url
    save_urls(urls)
    return short_code

def retrieve_url(short_code):
    urls = load_urls()
    return urls.get(short_code, "URL not found.")
