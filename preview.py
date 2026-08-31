# -*- coding: utf-8 -*-
"""
本地预览脚本：启动一个静态服务器，以便在浏览器中正常预览（含 3D 模型）。
运行方式：双击 start_preview.bat，或在命令行执行  py preview.py
会自动用浏览器打开本页，按 Ctrl+C 停止。
"""
import http.server
import os
import socket
import webbrowser

# 切换到脚本所在目录，保证能找到 assets / index.html
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 找一个空闲端口
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 0))
    PORT = s.getsockname()[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass  # 静默日志，避免刷屏


url = "http://127.0.0.1:%d/index.html" % PORT

print("=" * 46)
print("  本地预览已启动（支持 3D 模型）")
print("  网址： %s" % url)
print("  按 Ctrl + C 停止")
print("=" * 46)

try:
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), QuietHandler)
    webbrowser.open(url)
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n已停止。")
