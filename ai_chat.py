import os
import setting,help
import logging as log
from file_creater import load_config

CONFIG_DIR='config_file'
HISTORY_AI_DIR='history_for_ai'

def chat(messages,client):
    #==================ai对话主体=============================
    while True:
        #其他判断
        user_input=input("你: ")
        config=load_config(CONFIG_DIR)
        if config['clear_screen']==1:
            os.system('cls')
            print('你：'+user_input)
            log.info(f'用户：{user_input}')
        if user_input=="exit":
            yorn=input('y/n:')
            if yorn=='y':
                break
        elif user_input=='setting_yes':
            messages=setting.setting(messages)
            continue
        elif user_input=='help':
            help.help()
            continue
        #对话
        messages.append({"role": "user", "content": user_input})    
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )
        reply=response.choices[0].message.content    
        messages.append({"role": "assistant", "content": reply})
        print("AI: ", reply)
        log.info(f"AI:{reply}")
        #写入历史记录
        with open(os.path.join(HISTORY_AI_DIR, 'messages.txt'),'w',encoding="utf-8") as history:
            history.write(str(messages))