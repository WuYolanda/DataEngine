#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-


import pandas as pd

# 导入数据
df = pd.read_csv("car_complain.csv")

# 数据预处理
df = df.drop("problem", axis = 1).join(df.problem.str.get_dummies(','))

# 数据清洗，别名合并
def f(x):
    x = x.replace("一汽-大众","一汽大众")
    return x

# 品牌投诉总数
df['brand'] = df['brand'].apply(f)
df1 = df.groupby(['brand'])['id'].agg(['count']).sort_values('count', ascending = False)
print("品牌投诉总数")
print(df1)

# 车型投诉总数
df2 = df.groupby(['car_model'])['id'].agg(['count']).sort_values('count', ascending = False)
print("车型投诉总数")
print(df2)

# 品牌的平均车型投诉
df3 = df.groupby(['brand','car_model'])['id'].agg(['count'])
df3 = df3.groupby(['brand']).mean().sort_values('count', ascending = False)
print("品牌的平均车型投诉")
print(df3)
