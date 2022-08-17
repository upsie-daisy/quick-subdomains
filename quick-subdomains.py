##################
#
# A Handy Script for Finding Sub-Domains
#
# github.com/upsie-daisy/quick-subdomains
# Made by @Upsie-Daisy
#
#################

import requests, sys
from src.flags import Flag
from src.ansi import a

def add_subdomain(url):
    global subdomains
    for subdomain in subdomains:
        if subdomain == url:
            return
    subdomains.append(url)

def google_dorks(target="google.com"):
    try:
        from googlesearch import search
    except ImportError:
        print(f"{a.bl}[{a.r}x{a.bl}] {a.rst}No module named 'google' found (pip install google)")
        sys.exit(1)
        
    for url in search(f"site:*.{target}", tld="co.in", num=100, stop=10, pause=2):
        if url.startswith("https://"):
            url = url[8:]
        elif url.startswith("http://"):
            url = url[7:]
        url = url.split("/", 1)[0]

        add_subdomain(url)

def cert_spotter(target="google.com", api_key=""):
    headers = {}
    if api_key != "":
        headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(f"https://api.certspotter.com/v1/issuances?domain={target}&include_subdomains=true&expand=dns_names&expand=issuer&expand=cert", headers=headers)
    data = response.json()

    if response.status_code == 200:
        for certificate in data:
            for dns_name in certificate["dns_names"]:
                add_subdomain(dns_name)
    else:
        print(f"{a.bl}[{a.r}x{a.bl}] {a.rst}Error: Status code {response.status_code} ”{a.bl}{response.text}{a.rst}”")
        sys.exit(1)

flag = Flag(description="A Handy Script for Finding SubDomains, made by @Upsie-Daisy")

flag.new(short="-u", full="--url", required=True, help="Choose Target URL")
flag.new(short="-a", full="--api-key", help="certspotter.com API key")

flag.parse()

target = flag.url
api_key = flag.apikey

subdomains = []

cert_spotter(target, api_key)
google_dorks(target)

print(f"{a.bl}[{a.g}v{a.bl}] {a.bld}{a.c}Found {len(subdomains)} subdomains :\n")

for subdomain in subdomains:
    print(f"{a.bl}- {a.rst}{subdomain}")