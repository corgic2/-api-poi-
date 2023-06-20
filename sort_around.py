import pandas as pd
import math
import matplotlib.pyplot as plt
data = pd.read_csv("table4.csv")

position = [114.39909,30.50532]
x = position[0]
y = position[1]


for i in range(0, data.shape[0]):
    data.at[i, '店铺类别'] = data.at[i, '店铺类别'].split(';')[0]
    # print(data.iloc[i]['店铺类别'].split(';'))
# print(data)


def get_distance(x1, y1, x2, y2):
    t1 = (x1 - x2) * (x1 - x2)
    t2 = (y1 - y2) * (y1 - y2)
    return math.sqrt(t1 + t2)


poi_list_y = data['店铺具体坐标.纬度']
poi_list_x = data['店铺具体坐标.经度']
dis_list = []
for i in range(0,data.shape[0]):
    dis_list.append(get_distance(x, y, poi_list_x[i],poi_list_y[i]))

data['dis'] = dis_list

print(data)

sort_list = {}
dis_data = []
for i in range(0,len(dis_list)):
    if dis_list[i] < 0.02:
        if data.iloc[i]['店铺类别'] in sort_list.keys():
            sort_list[data.iloc[i]['店铺类别']] += 1
        else:
            sort_list[data.iloc[i]['店铺类别']] = 1

fig, ax = plt.subplots()

ax.bar(sort_list.keys(), sort_list.values())

ax.set_title("与光谷广场坐标小于0.2的店铺类别   ")
ax.set_xlabel("店铺类别  ")
ax.set_ylabel("店铺个数  ")


# 解决乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 20
plt.rcParams['axes.unicode_minus'] = False

plt.xticks(rotation=45)
plt.show()