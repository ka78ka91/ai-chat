#============================导入========================
from openai import OpenAI
import os
import time
import ai_chat
import api
import sys
import logging
from file_creater import file_creater,load_config
sys.dont_write_bytecode=True
#==========================log参数===========================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log.log', encoding='utf-8'),                              
    ]
)
#==========================常量定义============================
CONFIG_DIR='config_file'
HISTORY_DIR='history'
HISTORY_AI_DIR='history_for_ai'
API_KEY_DIR='api_key'
#========================变量定义==============================
keyfile=None
messages=[]
folder=API_KEY_DIR
#=======================文件创建================================
file_creater(API_KEY_DIR, CONFIG_DIR, HISTORY_DIR, HISTORY_AI_DIR)
#==========================对话================================
key=api.api_ready(folder)
client=OpenAI(api_key=key, base_url="https://api.deepseek.com/v1")
os.system('cls')
ai_chat.chat(messages,client)