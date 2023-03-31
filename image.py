from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
img = np.array(Image.open('b.png').convert("L"))
rows,cols=img.shape #获取图像的行数和列数
print(img)
for i in range(rows):
    for j in range(cols//2):
        img[i,j],img[i,cols-j-1]=img[i,cols-j-1],img[i,j]
plt.figure("1.bmp")
plt.imshow(img,cmap="gray") 
plt.axis("off")
plt.show( )