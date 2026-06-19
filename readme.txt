使用说明
一、程序简介

这是一个基于DeepSeek API的AI对话程序，通过命令行窗口进行交互，支持多密钥管理、对话历史保存与导入、个性化设置等功能。

二、安装与配置

安装Python
确保电脑已安装Python 3.8或更高版本
在终端输入 python --version 检查版本

安装依赖库
在终端输入：pip install openai

获取API密钥
访问DeepSeek开放平台（platform.deepseek.com）
注册账号并创建API Key
复制密钥（格式为 sk-xxxxx）

运行程序
双击运行 main.py
或在终端输入：python main.py

三、基本指令

exit 退出程序
help 显示帮助信息
setting_yes 打开设置菜单

四、对话功能

直接输入文字即可与AI对话，AI会记住所有历史对话内容

示例：
你：你好
AI：你好！有什么可以帮你的吗？

你：帮我写一个快速排序
AI：好的，以下是Python快速排序代码...

五、设置菜单

输入 setting_yes 进入设置菜单，显示以下选项：

每次打开窗口时，提示检测到默认密钥

保存当前对话历史

导入对话历史

每轮对话完后清空控制台输出

各项功能说明：

配置1：默认密钥提示
开启：每次启动询问是否使用默认密钥
关闭：直接使用默认密钥，不询问

配置2：保存对话历史
将当前对话保存到 history 文件夹

配置3：导入对话历史
导入之前保存的对话历史文件，继续对话

配置4：每轮清屏
开启：每次输入后自动清屏
关闭：保留屏幕内容

六、文件说明

api_key/ API密钥存放文件夹
default_api_key.txt 默认API密钥文件

config_file/ 配置文件存放文件夹
1 配置1：默认密钥提示开关（1=开启，0=关闭）
2 配置2：保存对话历史开关
3 配置3：导入对话历史开关
4 配置4：每轮清屏开关

history/ 用户保存的对话历史
1.txt 保存的对话历史文件
2.txt

history_for_ai/ AI自动保存的对话记录
messages.txt 当前对话自动保存

七、配置文件说明

配置项 文件 1=开启 0=关闭
默认密钥提示 config_file/1 开启 关闭
保存对话历史 config_file/2 开启 关闭
导入对话历史 config_file/3 开启 关闭
每轮清屏 config_file/4 开启 关闭

八、常见问题

报错 No module named 'openai'
解决：在终端输入 pip install openai

报错 FileNotFoundError: config_file/1
解决：运行 main.py 会自动创建配置文件

中文显示乱码
解决：在终端输入 chcp 65001 后重新运行

API密钥无效
解决：检查 api_key/default_api_key.txt 中的密钥是否正确
或删除该文件重新运行，输入新密钥

九、文件结构树

ai/
├── main.py 主程序入口
├── api.py API密钥管理模块
├── ai_chat.py AI对话核心模块
├── setting.py 设置管理模块
├── 使用说明.txt 本文件
│
├── api_key/ API密钥存放文件夹
│ └── default_api_key.txt 默认API密钥文件
│
├── config_file/ 配置文件存放文件夹
│ ├── 1 配置1：默认密钥提示开关
│ ├── 2 配置2：保存对话历史开关
│ ├── 3 配置3：导入对话历史开关
│ └── 4 配置4：每轮清屏开关
│
├── history/ 用户保存的对话历史
└── history_for_ai/ AI自动保存的对话记录
└── messages.txt 当前对话自动保存

