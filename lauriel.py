#! /usr/bin/env python

import csv
from setup_crawler import gather_webaddr, validate_webaddr


def lauriel():
    starting_website = input("Input url of a website you wish to 'scan': ")
    while True:
        try:
            raw_websites = gather_webaddr(starting_website)
            validated_websites = validate_webaddr(raw_websites)
            with open("websites.csv", "wb") as csvfile:
                f = csv.writer(csvfile, delimeter=',')
                f.writerow(validated_websites)
        except (KeyboardInterrupt, SystemExit):
            print("KeyboardInterrupt has bit raised")
            break


if __name__ == "__main__":
    lauriel()
