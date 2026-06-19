import os
import time
from openai import OpenAI
import logging as log
from file_creater import load_config 

CONFIG_DIR='config_file'
API_KEY_DIR='api_key'
DEFAULT_KEY_FILE='default_api_key.txt'

def api_ready(key_dir):
#=========================api准备=====================
    try:
        with open(os.path.join(API_KEY_DIR, DEFAULT_KEY_FILE),'r',encoding="utf-8") as key_file:
            key=key_file.read()
            config=load_config(CONFIG_DIR)
            if config['key_prompt']==1:
                yorn=input("检测到默认api密钥'"+key+"'存在是否使用(y/n)")
                os.system('cls')
                if yorn=='y':
                    key=key
                elif  yorn=='n':
                    key_name=input('请输入的使用api密钥名称:')
                    os.system('cls')
                    path=os.path.join(key_dir, key_name+'.txt')
                    try:
                        with open(path,'r',encoding="utf-8") as key_file:
                            key=key_file.read()
                        log.info('已使用自定义api密钥,加载中...')
                        print('已使用自定义api密钥,加载中...')
                        time.sleep(1)
                    except FileNotFoundError as e:  
                        log.error('api密钥不存在: %s', e)
                        yorn=input('未找到文件'+path+'是否创建?')
                        os.system('cls')
                        if yorn=='y':
                            key_name=input('请输入将创建的api密钥名称')
                            os.system('cls')
                            path=os.path.join(key_dir, key_name+'.txt')
                            with open(path,'w',encoding="utf-8") as key_file:
                                key_file.write(key:=input('请输入将要创建的api密钥:'))
                            os.system('cls')
                            log.info('已使用创建的api密钥,加载中...')
                            print('已使用创建的api密钥,加载中...')
                            time.sleep(1)
                        elif yorn=='n':
                            log.info('已使用默认密钥,加载中...')
                            print('已使用默认密钥,加载中...')
                            time.sleep(1)
    except:
        key_name=DEFAULT_KEY_FILE
        path=os.path.join(key_dir, key_name)
        with open(path,'w',encoding="utf-8") as key_file:
            key_file.write(key:=input('请输入默认api密钥:'))
    return key