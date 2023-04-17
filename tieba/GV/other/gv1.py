import json
import math
import matplotlib
import matplotlib.pyplot as plt

# 读取 JSON 数据
with open('output/output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

level_counts = {}
ip_counts = {}
os_counts = {}
reply_counts = {}
total_count = len(data)
for d in data:
    level = int(d['author_level'])
    level_counts[level] = level_counts.get(level, 0) + 1
    ip = str(d['ip'])
    region = ip[5:]
    ip_counts[region] = ip_counts.get(region, 0) + 1
    os = d['os']
    os_counts[os] = os_counts.get(os, 0) + 1
    reply = int(math.log(int(d['reply'])+1, 2))
    reply_counts[reply] = reply_counts.get(reply, 0) + 1

labels = []
sizes = []
for level in range(1, max(level_counts.keys()) + 1):
    count = level_counts.get(level, 0)
    if count > 0:
        labels.append(f'{level}')
        sizes.append(count)

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle('用户等级统计图')
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')
ax2.bar(labels, sizes)
ax2.set_xlabel('用户等级')
ax2.set_ylabel('频数')
plt.savefig('output/用户等级统计图.png', dpi=300)
plt.close()

other_ip_count = 0
other_ip_label = '其他'
for ip, count in list(ip_counts.items()):
    if count/total_count < 0.01:
        other_ip_count += count
        ip_counts.pop(ip)
ip_counts[other_ip_label] = other_ip_count

labels = list(ip_counts.keys())
sizes = list(ip_counts.values())
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(sizes, labels=labels, autopct='%1.1f%%',pctdistance=0.9)
plt.axis('equal')
plt.title('IP地址统计图')
plt.savefig('output/IP地址统计图.png',dpi=300)
plt.close()

other_os_count = 0
other_os_label = '其他'
for os, count in list(os_counts.items()):
    if count/total_count < 0.01:
        other_os_count += count
        os_counts.pop(os)
os_counts[other_os_label] = other_os_count

labels = list(os_counts.keys())
sizes = list(os_counts.values())
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('客户端统计图')
plt.savefig('output/客户端统计图.png',dpi=300)
plt.close()

labels = []
sizes = []
for reply in range(1, max(reply_counts.keys()) + 1):
    count = reply_counts.get(reply, 0)
    if count > 0:
        labels.append(f'{reply}')
        sizes.append(count)
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(labels, sizes)
plt.title('帖子回复数统计图')
plt.xlabel('帖子回复取对数值')
plt.ylabel('频数')
plt.savefig('output/帖子回复数统计图.png', dpi=300)
plt.close()
