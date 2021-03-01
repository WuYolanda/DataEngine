from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt


# 数据加载
data = pd.read_csv("car_data.csv", encoding='gbk')
train_x = data[["人均GDP", "城镇人口比重", "交通工具消费价格指数", "百户拥有汽车量"]]
# 规范化到 [0,1] 空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)

# K-Means 手肘法：统计不同K取值的误差平方和
sse = []
for k in range(1, 11):
    # kmeans算法
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
    # 计算inertia簇内误差平方和
    sse.append(kmeans.inertia_)
x = range(1,11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()


def K_means(train_data, k):
    """
    KMeans聚类,训练聚类模型
    :param train_data: 训练数据
    :param k: 聚类值
    :return: predict_y预测聚类模型
    """
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(train_data)
    predict_y = kmeans.predict(train_data)
    return predict_y

if __name__ == '__main__':
    # 键盘输入k值
    k = input("请输入K值:")
    # 选定k，训练聚类模型
    predict_y = K_means(train_x,int(k))
    # 合并聚类结果，插入到原数据中
    result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
    result.rename({0: "聚类结果"}, axis=1, inplace=True)
    print(result)
    # 分组打印地区
    for item in sorted(result["聚类结果"].unique()):
        print('第{}组: '.format(item+1))
        record = result[result["聚类结果"] == item]
        print(record['地区'].values)
