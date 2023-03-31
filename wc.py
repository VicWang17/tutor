import collections
import matplotlib 
import jieba
import wordcloud as wc
import numpy as np
from PIL import Image

wcg = wc.WordCloud(background_color = "white",font_path='assets/deng.ttf')
text = open('data/data.txt',encoding='utf-8').read()
seg_list=jieba.cut(text)
f=collections.Counter(seg_list)
wcg.fit_words(f)
wcg.to_file('b.png')
