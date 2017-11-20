#! /usr/bin/env python

from bs4 import BeautifulSoup
import urllib3
import re


def gather_webaddr(url):

    """ Input url, output list of possible website addresses """

    http = urllib3.PoolManager()
    html = http.request('GET', url)
    soup = BeautifulSoup(html.data, 'html.parser')
    addr = [link['href'] for link in soup.find_all('a', href=True)]
    return addr


def validate_webaddr(websites, pat=".*http.*"):

    """ filter list of possible website addresses with provided pattern
            (design to work in conjunction with gather_webaddr funcion) """

    p = re.compile(pat)
    webs = [website for website in websites if p.match(website) is not None]
    return webs


def check_if_websites_are_reachable(websites):

    """
    Input list of valid urls. Function checks if passed urls are reachable
    """

    http = urllib3.PoolManager()
    reachable_urls = []

    for url in websites:
        html = http.request('GET', url)

        if html.status == 200:
            reachable_urls.append(url)
        else:
            print("{url} is unreachable".format(url=url))
    return reachable_urls


if __name__ == "__main__":
    print(gather_webaddr("http://surrounded.prv.pl"))

    x = gather_webaddr("http://surrounded.prv.pl")
    print(validate_webaddr(x, '.*http.*'))
