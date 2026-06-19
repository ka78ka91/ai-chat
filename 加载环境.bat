@echo off
chcp 65001 >nul
cls
echo ========================================
echo         安装 ai_chat运行环境
echo ========================================
echo.

echo 正在安装依赖库...
pip install openai >nul 2>&1

if errorlevel 1 (
    echo  安装失败，请检查网络连接
    echo 或手动运行: pip install openai
) else (
    echo  安装成功！
)

echo.
echo 按任意键退出...
pause >nul