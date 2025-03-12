import json
import matplotlib
import matplotlib.pyplot as plt

# 读取 JSON 数据
with open('output/output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 统计操作系统出现的次数
os_counts = {}
total_count = 0
for d in data:
    os = d['os']
    os_counts[os] = os_counts.get(os, 0) + 1
    total_count += 1

# 将频率低于 1% 的操作系统单独存储，并从字典中删除
other_os_count = 0
other_os_label = '其他'
for os, count in list(os_counts.items()):
    if count/total_count < 0.01:
        other_os_count += count
        os_counts.pop(os)
os_counts[other_os_label] = other_os_count

# 绘制饼图
labels = list(os_counts.keys())
sizes = list(os_counts.values())
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('客户端统计图')
plt.savefig('output/客户端统计图.png',dpi=300)
