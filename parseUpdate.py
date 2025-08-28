import json 
import os
from datetime import datetime
from connection import ROOT_PATH

def previously_viewed_item_check(item_list: list):

    data_file_path = None

    if os.name == "nt":
        data_file_path = f"{ROOT_PATH}\\data.json"
    elif os.name == "posix":
        data_file_path = f"{ROOT_PATH}/data.json"

    if not os.path.exists(data_file_path):
        json_file = open(data_file_path, "w")
        json.dump({}, json_file)
        json_file.close()

    json_file = open(data_file_path)
    data = json.load(json_file)
    json_file.close()

    previously_viewed_items = [key for key in data.keys()]
    new_items = []
    items_to_update = []

    labled_new_items = {}
    labled_items_to_update = {}
    for item in item_list:
        if item["item"] not in previously_viewed_items:
            new_items.append(item)
        else: # Check if the price has changed
            if data[item["item"]]["last_price"] != item["price"]:
                items_to_update.append(item)

    if len(new_items) > 0:
        print("There are unseen items.")

        json_file = open(data_file_path)
        data = json.load(json_file)
        json_file.close()

        for item in new_items:
            data[item["item"]] = {
                "title": item["title"],
                "price": item["price"], 
                "last_price": item["price"],
                "original_price": item["price"], 
                "viewed": str(datetime.now()), 
                "updated": str(datetime.now())
            }
            labled_new_items[item["item"]] = data[item["item"]]

        with open(data_file_path, "w") as json_file:
            json.dump(data, json_file)
            json_file.close()
   
    if len(items_to_update) > 0:
        print("There are items with updated prices")

        json_file = open(data_file_path)
        data = json.load(json_file)
        json_file.close()

        for item in items_to_update:
            data[item["item"]] = {
                "title": item["title"],
                "price": item["price"], 
                "last_price": data[item["item"]]["price"],
                "original_price": data[item["item"]]["original_price"],
                "viewed": data[item["item"]]["viewed"], 
                "updated": str(datetime.now())
            }
            labled_items_to_update[item["item"]] = data[item["item"]]

        with open(data_file_path, "w") as json_file:
            json.dump(data, json_file)
            json_file.close()

    if len(labled_new_items) > 0 or len(labled_items_to_update) > 0:
        print(f"Sending new items to line_msg {labled_new_items}")
        print(f"Sending updated items to line_msg {labled_items_to_update}")
        return labled_new_items, labled_items_to_update

    if len(labled_new_items) == 0 and len(labled_items_to_update) == 0:
        print("There are no new items")
        return False
   