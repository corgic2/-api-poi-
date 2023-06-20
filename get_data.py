import requests
import pymongo
from trans import gcj02_to_wgs84

data_list = []

# 输入的URL
param = "key=b2bd757c75a52c67c80bebc0ab5d3248" \
        "&location=114.39909,30.50532" \
        "&page_size=20" \
        "&types=080000" \
        "&radius=10000"

inputUrl = "https://restapi.amap.com/v5/place/around?" + param


def get_data(url, page):
    newurl = url + "&page_num=" + str(page)
    response = requests.get(newurl)

    # 返回结果，JSON格式
    resultAnswer = response.json()
    # 返回结果中的状态标签，1为成功，0为失败
    resultStatus = resultAnswer['status']

    # print(resultAnswer)
    if resultStatus == '1':  # 返回成功
        # 读取返回的POI列表
        resultList = resultAnswer['pois']
        print(resultList)
        if len(resultList) == 0:  # 返回的POI列表为空
            return False
        else:
            # 返回的POI列表不为空，则遍历读取所有的数据，并写入到data xlsx中
            for j in range(0, len(resultList)):
                saveName = str(resultList[j]['name'])  # POI名称
                saveType = str(resultList[j]['type'])  # POI类别
                saveprovi = str(resultList[j]['pname'])  # POI省份
                savecity = str(resultList[j]['cityname'])  # POI城市
                savead = str(resultList[j]['adname'])  # POI地区
                saveAddress = str(resultList[j]['address'])  # POI地址
                saveposition = str(resultList[j]['location'])  # POI坐标
                saveposition_x = saveposition.split(',')[0]
                saveposition_y = saveposition.split(',')[1]
                dict_data = {"店铺名称": saveName, "店铺类别": saveType, "店铺所在省份": saveprovi,
                             "店铺所在城市": savecity, "店铺所在地区": savead, "店铺具体地址": saveAddress,
                             "店铺具体坐标": {"经度": saveposition_x, "纬度": saveposition_y}}
                data_list.append(dict_data)
            return True
    else:
        print("当前返回结果错误！")


def connect_mongodb_insert_data(data, table):
    myclient = pymongo.MongoClient("mongodb://hadoop102:27017")
    db = myclient["python"]
    coll = db[table]
    for i in data:
        coll.insert_one(i)
    print("插入数据到mongodb成功")


# get_data(inputUrl, 1)

for i in range(0, 100):
    if not get_data(inputUrl, i + 1):
        break

connect_mongodb_insert_data(data_list, 'table3')

# 将高德地图坐标转化为wgs84坐标系下的坐标
for i in data_list:
    # print(i['店铺具体坐标'])
    x = float(i['店铺具体坐标']['经度'])
    y = float(i['店铺具体坐标']['纬度'])
    poisition = gcj02_to_wgs84(x, y)
    i['店铺具体坐标']['经度'] = poisition[0]
    i['店铺具体坐标']['纬度'] = poisition[1]
    # print(i['店铺具体坐标'])

connect_mongodb_insert_data(data_list, 'table4')