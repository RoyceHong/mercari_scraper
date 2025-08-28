#!env/bin/python

from dotenv import load_dotenv
from connection import Mercari, ROOT_PATH
import os
import json
import parseUpdate
import message
import argparse


load_dotenv()

mercari_api = Mercari()

parser = argparse.ArgumentParser(prog="test.py", description="Automatically search Mercari and send all unseen items to your line account")

parser.add_argument("keyword", help="Search keyword")
parser.add_argument("--price-min")
parser.add_argument("--price-max")
parser.add_argument("-e", "--electronics", help="Search all electronics", action="store_true")
parser.add_argument("-c", "--computers", help="Search specifically for computer related items", action="store_true")
parser.add_argument("-p", "--pc-parts", help="Search even more specifically for pc parts", action="store_true")

args = parser.parse_args()


    

if __name__ == "__main__":
    print("Checking Mercari for items")
    results = mercari_api.fetch_items_pagination(
        keyword=args.keyword,
        price_min=args.price_min,
        price_max=args.price_max,
        e_flag=args.electronics,
        c_flag=args.computers,
        p_flag=args.pc_parts)
    print(f"There are {len(results)} results")

    print("Checking to see if items have been previously seen")
    items_to_message = parseUpdate.previously_viewed_item_check(results)

    if items_to_message is not False:
        message.local_msg(items_to_message)
