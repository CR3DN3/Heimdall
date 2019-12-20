#!/usr/bin/env python3

import argparse
from datetime import datetime

from src import color as C
from src import banner as B
from src import help as Help

from lib import exploit as Exploit

parser = argparse.ArgumentParser(description="Simple, powerful, fast and easy to use code can use",
                                 add_help=False)

parser.add_argument("-h", "--help",
                    action="store_true",
                    help="Show this help message and exit")

parser.add_argument("-u", "--url",
                    action="store",
                    type=str,
                    default=False,
                    help="Target URL (http://www.site.com/)")

parser.add_argument("--wordlist",
                    action="store",
                    type=str,
                    default="1",
                    help="Set wordlist. Default: 1 (Small) and Max: 3 (Big)")

parser.add_argument("--user-agent",
                    action="store",
                    type=str,
                    default=False,
                    help="Customize the User-Agent. Default: Random User-Agent")

args = parser.parse_args()

if args.url == False:
    print(C.BOLD, C.YELLOW + B.Banner + C.RESET)
    print(Help.Message)
    exit()
else:
    print(C.BOLD, C.YELLOW + B.Banner + C.RESET)
    print ("{}[+]{} Started!  Date: {} Time: {}".format(C.GREEN, C.RESET, datetime.now().strftime("%m/%d/%Y"), datetime.now().strftime("%H:%M")))
    Exploit.Finder(args)