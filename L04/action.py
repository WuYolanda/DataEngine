import pandas as pd
from efficient_apriori import apriori

# 加载数据
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None) 
# 查看数据
print(dataset.shape)
print(dataset)

# 将数据存放到transactions中
transactions = []
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, 20):
        if str(dataset.values[i, j]) != 'nan':
           temp.append(str(dataset.values[i, j]))
    transactions.append(temp)
# print(transactions)

# 挖掘频繁项集和频繁规则
itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.4)
print("频繁项集：", itemsets)
print("关联规则：", rules)
