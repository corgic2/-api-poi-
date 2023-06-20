import pandas as pd
import math
import matplotlib.pyplot as plt

data = pd.read_excel("购物服务.xlsx")
data1 = pd.read_excel("餐馆.xlsx")
data2 = pd.read_excel("生活服务.xlsx")

position = [114.22964, 30.65843]
x = position[0]
y = position[1]





# 购物服务
poi_list_y = data['店铺具体坐标.纬度']
poi_list_x = data['店铺具体坐标.经度']
size_poi = [1 for i in range(len(poi_list_x))]
plt.scatter(poi_list_x, poi_list_y, sizes=size_poi, c='blue')

# 餐馆
poi_list_y_1 = data1['店铺具体坐标.纬度']
poi_list_x_1 = data1['店铺具体坐标.经度']
size_poi_1 = [1 for i in range(len(poi_list_x_1))]
plt.scatter(poi_list_x_1, poi_list_y_1, sizes=size_poi_1, c='green')

# 生活服务
poi_list_y_2 = data2['店铺具体坐标.纬度']
poi_list_x_2 = data2['店铺具体坐标.经度']
size_poi_2 = [1 for i in range(len(poi_list_x_2))]
plt.scatter(poi_list_x_2, poi_list_y_2, sizes=size_poi_2, c='#FFD700')

plt.plot(position[0], position[-1], 'ro', markersize=5)

plt.xlabel("经度  廖峰 张冰冰 数据挖掘作业数据分析模块")
plt.ylabel("纬度  时间:2023年6月4日20点58分")

# 解决乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 20
plt.rcParams['axes.unicode_minus'] = False

plt.show()
