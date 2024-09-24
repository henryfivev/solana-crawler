import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 读取嵌入向量和对应的标签
embeddings_df = pd.read_csv('embeddings.csv')
# 假设 labels 是你的标签数据
labels = [...]  # 你需要提供的标签列表，与 embeddings 一一对应

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(embeddings_df, labels, test_size=0.2, random_state=42)

# 创建 DMatrix 数据格式
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test)

# 设置参数并训练模型
params = {
    'objective': 'multi:softmax',  # 分类任务
    'num_class': len(set(labels)),  # 类别数
    'max_depth': 3,
    'eta': 0.1,
    'silent': 1
}
model = xgb.train(params, dtrain, num_boost_round=100)

# 预测
preds = model.predict(dtest)

# 评估准确率
accuracy = accuracy_score(y_test, preds)
print(f"Accuracy: {accuracy:.2f}")
