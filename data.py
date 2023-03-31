import pandas as pd
import numpy as np
d = {'Name':pd.Series(['编程帮','编程帮',"百度",'搜索','谷歌','微学苑','B索']),
   'years':pd.Series([5,5,15,28,3,19,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8]),
     '性别':pd.Series(['男','男','女','男','女','女','女'])}

df = pd.DataFrame(d)

g = df.groupby("性别",as_index = False)

print(df['Name'])

























 















