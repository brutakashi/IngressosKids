import requests
from xml.etree import ElementTree as ET

def process_url(url):
    response = requests.get(url)
    # Faça algo com a resposta, por exemplo, imprimir o status
    print(f'URL: {url} - Status Code: {response.status_code}')

def process_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    sitemap = ET.fromstring(response.content)
    
    for url in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        process_url(url.text)

if __name__ == "__main__":
    sitemap_url = "https://www.ingressoskids.com/sitemap.xml"  # Substitua pela URL real do seu sitemap
    process_sitemap(sitemap_url)
