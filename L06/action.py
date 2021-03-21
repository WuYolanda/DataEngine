import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

# 读入数据集
df = pd.read_csv('./train.csv')
df['Datetime'] = pd.to_datetime(df.Datetime, format='%d-%m-%Y %H:%M')
df.index = df.Datetime
df.drop(['ID', 'Datetime'], axis=1, inplace=True)
# 按天聚合
daily_df = df.resample('D').sum()
# 将时间顺序列名修改符合Prophet要求
daily_df['ds'] = daily_df.index
daily_df['y'] = daily_df.Count
daily_df.drop('Count', axis=1, inplace=True)
print(daily_df.head())

# 拟合Prophet模型
model = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
model.fit(daily_df)
# 预测未来七个月（213天）
future = model.make_future_dataframe(periods=213)
forcast = model.predict(future)
# print(forcast)

# 查看预测各成份
model.plot_components(forcast)

# 绘制预测
model.plot(forcast)
plt.show()

