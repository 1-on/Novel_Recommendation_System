import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

novels = pd.read_csv('novels1.csv')
history = pd.read_csv('history.csv')

# 将类型和作者合并为一个字符串
novels['features'] = novels['小说类型'] + ' ' + novels['作者名称']

# 创建一个TfidfVectorizer对象
vectorizer = TfidfVectorizer()

# 将特征字符串转换为TF-IDF矩阵
tfidf_matrix = vectorizer.fit_transform(novels['features'])

# 计算小说之间的余弦相似度。
similarity_matrix = cosine_similarity(tfidf_matrix)

# 将相似度矩阵转换为一个DataFrame
similarity_df = pd.DataFrame(similarity_matrix, index=novels['小说名称'], columns=novels['小说名称'])


# def get_recommendations(novel, similarity_df, top_n=10):
#     similarity_scores = similarity_df[novel]
#     top_novels = similarity_scores.sort_values(ascending=False).head(top_n + 1)
#     top_novels = top_novels.drop(novel)
#     return top_novels

def get_recommendations(novels_list, similarity_df, top_n=5):
    # 初始化一个空的Series对象，用于存储相似度分数
    total_similarity_scores = pd.Series(dtype=float)

    # 遍历输入的小说列表
    for novel in novels_list:
        # 获取当前小说的相似度分数
        similarity_scores = similarity_df[novel]

        # 将当前小说的相似度分数累加到总分数中
        total_similarity_scores = total_similarity_scores.add(similarity_scores, fill_value=0)

    # 计算平均相似度分数
    avg_similarity_scores = total_similarity_scores / len(novels_list)

    # 获取前n个最相似的小说
    top_novels = avg_similarity_scores.sort_values(ascending=False).head(top_n + len(novels_list))

    # 从推荐列表中移除输入的小说
    for novel in novels_list:
        top_novels = top_novels.drop(novel, errors='ignore')

    return top_novels.head(top_n)


# last_read_novel = history.iloc[-1]['小说名称']
#
# recommendations = get_recommendations(last_read_novel, similarity_df)
read_novels = history['小说名称'].tolist()
recommendations = get_recommendations(read_novels, similarity_df)

print("Recommended novels based on your last read novel:")
for novel_name in recommendations.index:
    print(novel_name)
print(recommendations)
