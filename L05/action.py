import pandas as pd
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt


# 数据加载
data = pd.read_csv("Market_Basket_Optimisation.csv",header=None)
# print(data)

# 将数据存放操transactions中
transactions = []
# 存储字典key:value
item_count = {}
for i in range(data.shape[0]):
	temp = []
	for j in range(data.shape[1]):
		item = str(data.values[i, j])
		if item != "nan":
			temp.append(item)
			if item not in item_count:
				item_count[item] = 1
			else:
				item_count[item] += 1
	transactions.append(temp)

# 去掉停用词
def remove_stop_words(f):
	stop_words = []
	for stop_word in stop_words:
		f = f.replace(stop_word, '')
	return f

# 生成词云
def create_word_cloud(f):
	print('根据词频，开始生成词云!')
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()


# 生成词云
all_word = " ".join("%s" %item for item in transactions)
# print(all_word)
create_word_cloud(all_word)

# Top10的商品有哪些
print("Top10的商品有:")
print(sorted(item_count.items(),key=lambda x:x[1],reverse=True)[:10])