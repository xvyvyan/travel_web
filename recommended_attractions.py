import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# 加载数据
data = pd.read_csv("")

# 对数据进行预处理，例如去除缺失值
data.dropna(inplace=True)

# 计算景点之间的相似度
similarity = cosine_similarity(data)

# 获取推荐景点
def recommend(scenic_id, top_k=5):
    scores = similarity[scenic_id]
    scenic_index = np.argsort(-scores)
    return scenic_index[1:top_k+1]

# 输入一个景点ID，获取推荐景点
recommended_scenic = recommend(0)
print(recommended_scenic)
