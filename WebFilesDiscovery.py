import requests
import re
import urllib.parse
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="target_url", help="Speify URL, -h For Help")
    options, arguments = parser.parse_args()

    if not options.target_url:
        parser.error("[-] Please specify url, -h for help")

    return options.target_url

target_url = get_arguments()
target_links = []

def get_links(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode())

def crawl(url):
    href_links = get_links(url)
    for link in href_links:
        link = urllib.parse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if url in link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)