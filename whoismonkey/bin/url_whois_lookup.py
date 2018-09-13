#!/usr/bin/env python

import csv
import sys
import os
import urllib

""" 
   An adapter that takes CSV as input, performs a whois lookup, then returns a JSON response into the CSV results 
"""


#WHOISURL='http://x.x.x.x.us-west-2.compute.amazonaws.com:5000/query/?domain='
WHOISURL='http://localhost:5000/query/?domain='

# Whois request
def lookup(ip):
    try:
        whois_ret = urllib.urlopen(WHOISURL + ip)
        lines = whois_ret.readlines()
        return lines
    except:
        return []


def main():
    if len(sys.argv) != 3:
        print "Usage: python external_lookup_whois.py [whois field] [ip field]"
        sys.exit(1)

    whoisfield = sys.argv[1]
    ipfield = sys.argv[2]

    infile = sys.stdin
    outfile = sys.stdout

    r = csv.DictReader(infile)
    header = r.fieldnames

    w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
    w.writeheader()

    for result in r:
        # Perform the lookup or reverse lookup if necessary
        if result[whoisfield] and result[ipfield]:
            # both fields were provided, just pass it along
            w.writerow(result)

        elif result[whoisfield]:
            ips = lookup(result[whoisfield])
            for ip in ips:
                result[ipfield] = ip
                w.writerow(result)

        elif result[ipfield]:
            result[whoisfield] = lookup(result[ipfield])
            if result[whoisfield]:
                w.writerow(result)


main()
