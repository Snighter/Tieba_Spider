import json
import matplotlib
import matplotlib.pyplot as plt

# 读取 JSON 数据
with open('output/output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 统计 author_level 出现的次数
level_counts = {}
for d in data:
    level = int(d['author_level'])
    level_counts[level] = level_counts.get(level, 0) + 1

# 按顺序排列各个等级
labels = []
sizes = []
for level in range(1, max(level_counts.keys()) + 1):
    count = level_counts.get(level, 0)
    if count > 0:
        labels.append(f'{level}')
        sizes.append(count)

# 绘制饼图
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle('用户等级统计图')

ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')

# 绘制直方图
ax2.bar(labels, sizes)
ax2.set_xlabel('用户等级')
ax2.set_ylabel('频数')

# 保存图片
plt.savefig('output/用户等级统计图.png', dpi=300)
