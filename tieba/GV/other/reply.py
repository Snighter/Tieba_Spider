import json
import math
import matplotlib
import matplotlib.pyplot as plt

# 读取 JSON 数据
with open('output/output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 统计 reply 出现的次数
reply_counts = {}
for d in data:
    reply = int(math.log(int(d['reply'])+1, 2))
    reply_counts[reply] = reply_counts.get(reply, 0) + 1

# 按顺序排列各个等级
labels = []
sizes = []
for reply in range(1, max(reply_counts.keys()) + 1):
    count = reply_counts.get(reply, 0)
    if count > 0:
        labels.append(f'{reply}')
        sizes.append(count)

# 绘制饼图
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(labels, sizes)
plt.title('帖子回复数统计图')
plt.xlabel('帖子回复数')
plt.ylabel('频数')
plt.savefig('output/帖子回复数统计图.png', dpi=300)
