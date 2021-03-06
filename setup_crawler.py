#! /usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import re


def gather_webaddr(url):

    """ Input url, output list of possible website addresses """

    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, from_encoding=html.info().getparam('charset'))
    addr = [link['href'] for link in soup.find_all('a', href=True)]
    return addr


def validate_webaddr(websites, pat=".*http.*"):

    """ filter list of possible website addresses with provided pattern
            (design to work in conjunction with gather_webaddr funcion) """

    p = re.compile(pat)
    webs = [website for website in websites if p.match(website) is not None]
    return webs


if __name__ == "__main__":
    print(gather_webaddr("http://surrounded.prv.pl"))

    x = gather_webaddr("http://surrounded.prv.pl")
    print(validate_webaddr(x, '.*http.*'))
