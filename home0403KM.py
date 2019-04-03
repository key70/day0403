import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

path = "C:/Windows/Fonts/malgun.ttf"
rc('font', family=font_manager.FontProperties(fname=path).get_name())


# f = open('./Data/2016_GDP.txt','r',encoding='utf-8')
data = []
with open('./Data/2016_GDP.txt','r',encoding='utf-8') as f:
    for item in f:
        item = item.replace('\n','').split(':')
        data.append(item)

# print(data)
del data[0]
gdp = []
name = []
for i in data:
    name.append(i[1])
    gdp.append(i[2].replace(",",""))


nameN = np.array(name)
gdpN = np.array(gdp,dtype=int)
sort = np.argsort(gdpN)[::-1]
# print(nameN[sort<10])
# print(gdpN[sort<10])
x_name = nameN[:10]
plt.bar(range(10),gdpN[:10],tick_label=x_name)
plt.title('국가별 gdp')
# plt.xcorr(range(10),nameN[sort<10])
plt.show()







# gdp = np.array(arr[:2],dtype='int32')
# print(gdp)
# name = arr[:,1]
# sort = np.argsort(arr[:,2])[::-1]
# print(type(sort))







# r = f.read()
# arr = np.array(r)



# a = np.array(r.split(':'))
# arr = a.reshape(-1)
# print(arr)
# print(arr[4])






f.close()

