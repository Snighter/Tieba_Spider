import os
import json
import jieba
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud

background_image = np.array(Image.open("GV\word_cloud\path_img.jpg"))

# 读取爬取的数据
with open('output/output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 将所有标题连接成一个字符串
titles = " ".join([d['title'] for d in data])
cut_text = " ".join([word for word in jieba.cut(titles) if len(word) >= 2 and "什么" not in word])


# 创建词云对象
wordcloud = WordCloud(
    scale=12,
    font_path="C:/Windows/Fonts/simfang.ttf",
    background_color="white", width=1860,
    height=2010, margin=0, mask=background_image).generate(cut_text)

# 显示词云图
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
if not os.path.exists('output'):
    os.mkdir('output')
wordcloud.to_file(os.path.join('output', '帖子标题词云统计图.png'))