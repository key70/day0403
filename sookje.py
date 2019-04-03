import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import re

path = "C:/Windows/Fonts/malgun.ttf"
rc('font', family=font_manager.FontProperties(fname=path).get_name())

txt = []
with open('Data/2016_GDP.txt','r',encoding='utf-8')as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(':')
        txt.append(cols)
del txt[0]
nation = []
gdp = []

for i in txt:
    n = i[1]
    g = i[2].replace(",","")
    nation.append(n)
    gdp.append(g)

nation1 = np.array(nation,dtype=str)
gdp1 = np.array(gdp,dtype=int)
gdp2 =np.argsort(gdp1)[::-1]
nation2 = np.argsort(nation1)[::-1]
gdp3 = gdp1[:10]
nation3 = nation1[:10]
print(nation3)
x_name = nation3
plt.bar(range(10),gdp3,tick_label=x_name)
plt.plot(range(10),gdp3,"yo")
plt.plot(range(10),gdp3)
plt.title("GDP 상위 10개 국가")
plt.ylabel('GDP')
plt.xlabel('국가')
plt.show()




cd
