# 🤖 AI 对话助手

一个基于 DeepSeek API 的命令行 AI 对话程序，支持多密钥管理、对话历史保存与导入、个性化设置等功能。

---

## ✨ 功能特性

- 💬 **AI 对话**：基于 DeepSeek API，支持上下文连续对话
- 🔑 **多密钥管理**：支持多个 API 密钥切换使用
- 💾 **对话历史**：自动保存当前对话，支持手动保存与导入
- ⚙️ **个性化设置**：
  - 默认密钥提示开关
  - 每轮对话后自动清屏
- 📝 **日志记录**：所有对话和操作记录到 `log.log` 文件
- 📦 **配置统一**：使用 JSON 格式管理配置

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install openai
2. 获取 API 密钥
访问 DeepSeek 开放平台 注册并创建 API Key

3. 运行程序
bash
python main.py
首次运行会提示输入默认 API 密钥，输入后自动保存。

📖 使用指南
基本指令
指令	作用
exit	退出程序
help	显示帮助信息
setting_yes	打开设置菜单
设置菜单
选项	功能
1	默认密钥提示开关
2	每轮清屏开关
3	保存对话历史
4	导入对话历史
📁 项目结构
text
ai-chat/
├── main.py              # 程序入口
├── ai_chat.py           # AI 对话核心逻辑
├── api.py               # API 密钥管理
├── setting.py           # 设置管理
├── file_creater.py      # 文件/配置创建
├── help.py              # 帮助信息
├── config_file/
│   └── config.json      # 配置文件
├── api_key/
│   └── default_api_key.txt  # 默认 API 密钥
├── history/             # 用户保存的对话历史
├── history_for_ai/      # 自动保存的对话记录
└── log.log              # 运行日志
🛠️ 技术栈
Python 3.8+

OpenAI SDK（DeepSeek API）

标准库：os, json, logging, ast, time

📝 常见问题
中文显示乱码
在终端执行：

bash
chcp 65001
python main.py
API 密钥无效
检查 api_key/default_api_key.txt 中的密钥是否正确，或删除该文件重新运行。

📄 许可证
MIT License

👨‍💻 作者
ka78ka91

⭐ 如果觉得有用，给个 Star 吧！