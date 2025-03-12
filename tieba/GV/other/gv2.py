import json
import math
import matplotlib.pyplot as plt

# 读取JSON数据
with open('output/output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 解析JSON数据，提取author_level和reply字段
author_levels = [int(d['author_level']) for d in data]
replies = [(math.log(int(d['reply'])+1, 2)) for d in data]

# 绘制散点图
plt.scatter(author_levels, replies,marker='.')
plt.xlabel('author_level')
plt.ylabel('log2(reply)')
plt.savefig('output/用户等级-回复数取对数值散点图.png', dpi=300)
