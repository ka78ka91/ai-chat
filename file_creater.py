import os
import json
default_config=\
{
    "key_prompt": 1,
    "save_history": 1,
    "import_history": 1,
    "clear_screen": 1
}
def file_creater(API_KEY_DIR,CONFIG_DIR,HISTORY_DIR,HISTORY_AI_DIR):
    #文件夹创建
    os.makedirs(API_KEY_DIR,exist_ok=True)
    os.makedirs(CONFIG_DIR,exist_ok=True)
    os.makedirs(HISTORY_DIR, exist_ok=True)
    os.makedirs(HISTORY_AI_DIR, exist_ok=True)
    #文件创建
    if not os.path.exists(os.path.join(CONFIG_DIR, 'config.json')):
        with open(os.path.join(CONFIG_DIR, 'config.json'),'w',encoding="utf-8") as configfile:
            json.dump(default_config, configfile, indent=2, ensure_ascii=False)
#加载配置
def load_config(CONFIG_DIR):
    config_path=os.path.join(CONFIG_DIR, 'config.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)
#写入配置
def upload_config(CONFIG_DIR,config):
    config_path=os.path.join(CONFIG_DIR, 'config.json')
    with open(config_path, 'w', encoding='utf-8') as f:
        return json.dump(config, f, indent=2, ensure_ascii=False)
