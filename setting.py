import os,time,ast
import logging as log
from file_creater import load_config,upload_config

CONFIG_DIR='config_file'
HISTORY_DIR='history'
def setting(chat_history):
    choice = input(
                    '请选择设置项\n'
                    '1.每次打开窗口时，提示检测到默认密钥\n'
                    '2.每轮对话完后清空控制台输出\n'
                    '3.保存当前对话历史\n'
                    '4.导入对话历史\n'
                    '请选择(1-4): '
                    )

    # 配置1
    if choice == '1':
        config=load_config(CONFIG_DIR)
        if config['key_prompt']==0:
            log.info('配置一已切换为开启')
            print('已切换为开启')
            config['key_prompt']=1
        else:
            log.info('配置一已切换为关闭')
            print('已切换为关闭')
            config['key_prompt']=0
        upload_config(CONFIG_DIR,config)
        print('加载中...')
        time.sleep(0.5)
        os.system('cls')
        return chat_history
    # 配置2
    if choice == '2':
        config=load_config(CONFIG_DIR)
        if config['clear_screen']==0:
            log.info('配置二已切换为开启')
            print('已切换为开启')
            config['clear_screen']=1
        else:
            log.info('配置二已切换为关闭')
            print('已切换为关闭')
            config['clear_screen']=0
        upload_config(CONFIG_DIR,config)
        print('加载中...')
        time.sleep(0.5)
        os.system('cls')
        return chat_history
    #配置3
    if choice=='3':
        while True:
            fillname=input('请输入文件名:')
            path=os.path.join(HISTORY_DIR, fillname+'.txt')
            try:
                with open(path) as test:
                    log.warning('文件名已存在')
                log.info('保存失败')
                print('保存失败,加载中...')
                time.sleep(0.5)
                os.system('cls')
            except:
                with open(path,'w',encoding='utf-8') as save:
                    save.write(str(chat_history))
                log.info('保存成功')
                print('保存成功,加载中...')
                time.sleep(0.5)
                os.system('cls')
                break
            os.system('cls')
        os.system('cls')
        return chat_history
    # 配置4
    if choice=='4':
        fillname=input('请输入文件名：').strip()
        path=os.path.join(HISTORY_DIR, fillname+'.txt')
        print(f"正在查找: {path}") 
        try:
            with open(path,'r',encoding="utf-8") as test:
                chat_history_new=test.read()
            log.info('导入成功')
            print('导入成功,加载中...')
            time.sleep(0.5)
            os.system('cls')
            return ast.literal_eval(chat_history_new)
        except Exception as e:
            log.warning(f"错误: {e}")
            log.warning("未找到文件'"+fillname+"'.txt")
            log.info('导入失败')
            print('导入失败,加载中...')
            time.sleep(0.5)
            os.system('cls')
            return chat_history
