#!/usr/bin/env python
import json
import subprocess
import time
from zapv2 import ZAPv2

# 启动 ZAP 应用程序
zap_path = 'C:\\Program Files\\ZAP\\Zed Attack Proxy\\zap.bat'  # 换成自己的 ZAP 安装路径
subprocess.Popen([zap_path])

# 等待 ZAP 完全启动并监听代理端口
time.sleep(16)  # 根据你的系统调整这个时间
apikey = 'nhocra6st486sshpdb54b2eopp' # Change to match the API key set in ZAP, or use None if the API key is disabled
#
# By default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apikey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
# zap = ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

# # browserTest
# firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'  # Firefox 安装路径
# os.startfile(firefox_path)

# 要加的：启动自动点击工具，打开已经与主机在同一局域网下，配置好系统级别CA证书的安卓设备的要测试的应用
# 自动点击工具遍历完毕，触发条件开始导包
# 若要一次性测多个应用，导出后关闭一下 subprocess ZAP, 重开循环

# 手动测试结束方法
input('ZAT START CAPTURING...\nENTER sth IF U WANT TO STOP:\n\n')

# 用时间规定控制结束时间
# time.sleep(8)

# 获取所有警报, 并将警报保存到 JSON 文件
try:
    alerts = zap.core.alerts()
    with open('zap_alerts.json', 'w') as json_file:
        json.dump(alerts, json_file, indent=4)
        print("所有警报已保存到 'zap_alerts.json' 文件中。")
except Exception as e:
    print(f"导出警报 JSON 文件时出错: {e}")

# 导出 对各站点警报总结 JSON 文件
try:
    json_report = zap.core.jsonreport()
    json_file_path = 'zap_export.json'
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_report)
    print(f"所有请求和响应数据已保存到 '{json_file_path}' 文件中。")
except Exception as e:
    print(f"导出各站点 JSON 文件时出错: {e}")

# 导出 HTTP/HTTPS 请求与响应的 HAR 文件
try:
    har_content = zap.core.messages_har()
    har_file_path = 'zap_export.har'
    with open(har_file_path, 'w', encoding='utf-8') as har_file:
        har_file.write(har_content)
    print(f"所有请求和响应数据已保存到 '{har_file_path}' 文件中。")
except Exception as e:
    print(f"导出 HAR 文件时出错: {e}")
