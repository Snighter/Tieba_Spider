import json
import matplotlib
import matplotlib.pyplot as plt

# 读取 JSON 数据
with open('output/output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 统计 ip 出现的次数
ip_counts = {}
total_count = 0
for d in data:
    ip = str(d['ip'])
    region = ip[5:]
    ip_counts[region] = ip_counts.get(region, 0) + 1
    total_count += 1

# 将频率低于 1% 的操作系统单独存储，并从字典中删除
other_ip_count = 0
other_ip_label = '其他'
for ip, count in list(ip_counts.items()):
    if count/total_count < 0.01:
        other_ip_count += count
        ip_counts.pop(ip)
ip_counts[other_ip_label] = other_ip_count

# 绘制饼图
labels = list(ip_counts.keys())
sizes = list(ip_counts.values())
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('IP地址统计图')
plt.savefig('output/IP地址统计图.png',dpi=300)
