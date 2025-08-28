from client import line_bot_api
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import os

def new_item_msg(new_items, item):
      return f"""
There is a new item.
{new_items[item]['title']}
Price: {new_items[item]['price']}円

Link: {item}"""

def update_item_msg(updated_items, item):
     return f"""
There is an updated item.

{updated_items[item]['title']}
New Price: {updated_items[item]['price']}円
Last Price: {updated_items[item]['last_price']}円
Original Price: {updated_items[item]['original_price']}円

Link: {item}"""
     

def line_msg(data_to_send):
    new_items, updated_items = data_to_send

    for item in new_items.keys():

        message = new_item_msg(new_items, item)

        try:
            line_bot_api.push_message(os.getenv("USER_ID"), TextSendMessage(text=message))
        except LineBotApiError as e:
            print(f"[ERROR]:{e}")

    for item in updated_items.keys():
            
            message = update_item_msg(updated_items, item)
    
            try:
                line_bot_api.push_message(os.getenv("USER_ID"), TextSendMessage(text=message))
            except LineBotApiError as e:
                print(f"[ERROR]:{e}")

def local_msg(data_to_send):
    new_items, updated_items = data_to_send

    for item in new_items.keys():

        message = new_item_msg(new_items, item)
        print(message)


    for item in updated_items.keys():
            
        message = update_item_msg
        print(message)