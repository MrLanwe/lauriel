#! /usr/bin/env python

import os
import csv
from setup_crawler import gather_webaddr, validate_webaddr


def lauriel():

    """ Input startin url or urls and lauriel will 'scan' all of the provided
    addresses and all addresses that were found during 'scanning'"""

    # TODO write a handler in validate_webaddr for website's that no longer
    # exist or are otherwise unreachable

    filename = 'websites.csv'
    urls_from_single_website = []
    starting_websites = input("Input url of a websites you wish to 'scan'"
                              "seperated by space: ")
    list_of_websites = starting_websites.split()

    if os.path.exists(filename):
        open_mod = 'a+'
    else:
        f = open(filename, 'w')
        f.close
        open_mod = 'a+'

    while True:

        print(list_of_websites)
        if 'validated_websites' in locals():
            list_of_websites = urls_from_single_website
            del urls_from_single_website[:]

        try:
            for url in list_of_websites:
                raw_websites = gather_webaddr(url)
                validated_websites = validate_webaddr(raw_websites)
                with open(filename, open_mod) as csvfile:
                    f = csv.writer(csvfile, delimiter=',')
                    f.writerow(validated_websites)

                urls_from_single_website += validate_webaddr
                print(url)
        except (KeyboardInterrupt, SystemExit):
                print("KeyboardInterrupt has bit raised")
                break


if __name__ == "__main__":
    lauriel()

