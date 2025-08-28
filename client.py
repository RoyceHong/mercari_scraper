from linebot import LineBotApi
import os
from dotenv import load_dotenv


load_dotenv()
# Create the singleton instance
line_bot_api = LineBotApi(os.getenv("CONNECTION_TOKEN"))