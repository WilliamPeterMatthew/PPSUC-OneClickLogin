import sys
import os
import requests
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def show_message(title, message):
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(resource_path("favicon.ico"))
    messagebox.showinfo(title, message)
    root.destroy()

def load_credentials():
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_path = os.path.join(script_dir, '账号密码.txt')
    
    if not os.path.exists(file_path):
        show_message("错误", "找不到账号密码.txt文件")
        sys.exit(1)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            username = f.readline().strip()
            password = f.readline().strip()
            if not username or not password:
                show_message("错误", "账号密码文件格式不正确")
                sys.exit(1)
            return username, password
    except Exception as e:
        show_message("错误", f"读取凭证失败: {str(e)}")
        sys.exit(1)

def perform_login(username, password):
    params = {
        'callback': 'dr1730552179698',
        'DDDDD': username,
        'upass': password,
        '0MKKey': '123456',
        'R1': '0',
        'R3': '0',
        'R6': '0',
        'para': '00',
        'v6ip': '',
        '_': generate_random(13)
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }

    try:
        response = requests.post(
            'http://192.168.8.123/drcom/login',
            params=params,
            headers=headers,
            timeout=15
        )
        response.raise_for_status()
        return parse_response(response)
    except requests.RequestException as e:
        return ("错误", f"网络请求失败: {str(e)}")

def generate_random(length):
    return str(int.from_bytes(os.urandom(length), byteorder='big'))[:length]

def parse_response(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else ''
    
    status_mapping = {
        "信息页": ("错误", "连接失败，账号或密码不正确"),
        "认证成功页": ("成功", "已连接（Code:200）")
    }
    
    return status_mapping.get(title, ("错误", f"未知响应状态（Title: {title}）"))

def main():
    root = tk.Tk()
    root.withdraw()
    
    try:
        username, password = load_credentials()
        status, message = perform_login(username, password)
        show_message(status, message)
    except Exception as e:
        show_message("错误", str(e))
    finally:
        root.destroy()

if __name__ == "__main__":
    main()
