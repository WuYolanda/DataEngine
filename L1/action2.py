#!/usr/bin/env python3.6
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# 创建DataFrame
data = np.array([[68, 65, 30],
                 [95, 76, 98],
                 [98, 86, 88],
                 [90, 88, 77],
                 [80, 90, 90]])
df = pd.DataFrame(data, index=["张飞", "关羽", "刘备", "典韦", "许褚"],
                  columns=["语文", "数学", "英语"])

# 计算各科平均成绩、最小成绩、最大成绩、方差和标准差
print("课程|平均成绩|最小成绩|最大成绩|方差|标准差")
for item in df.columns:
    print("{0} {1:.2f} {2} {3} {4:.2f} {5:.2f}"
          .format(item, np.mean(df[item]), np.min(df[item]), np.max(df[item]), np.var(df[item]), np.std(df[item])))

# 总成绩排序进行成绩输出
df["总分"] = df.sum(axis=1)
df = df.sort_values("总分", ascending=False)
print("总成绩从大到小排序：")
print(df)
