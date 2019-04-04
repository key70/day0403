import matplotlib.pyplot as plt
import numpy as np

info = []
with open('./Data/2016_GDP.txt','r',encoding='utf-8') as fp:
    for line in fp:
        line = line.strip().replace(",","")
        line = line.split(':')
        info.append(line)
        # print(line)

del info[0]
# print(info)

c_name = []
c_gdp = []
for g in info:
    c_name.append(g[1])
    c_gdp.append(g[2])
# print(c_gdp)

c_name2 = np.array(c_name)
c_gdp2 = np.array(c_gdp, dtype=np.int)

gdp2 =np.argsort(c_gdp2)[::-1] # 정렬
n = c_name2[:10]
# print(gdp2,c_gdp2[:10])
# print(n)

from matplotlib import font_manager, rc

rc('font', family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())

plt.bar(n,c_gdp2[:10], color = "pink")

plt.title("2016년 GDP_TOP10")
plt.show()