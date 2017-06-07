#! /usr/bin/env python

from setup_crawler import gather_webaddr, validate_webaddr


def lauriel():
    starting_website = raw_input("Input url of a website you wish to 'scan': ")
    raw_websites = gather_webaddr(starting_website)
    validated_websites = validate_webaddr(raw_websites)
