import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, accuracy_score, classification_report

dataset = './dataset/'

# 读取embeddings
phishing_embeddings = pd.read_csv(f'{dataset}phishing_embeddings.csv')
phishing_labels = pd.read_csv(f'{dataset}phishing_labels.csv')
phishing_labels = phishing_labels['label'].tolist()

nft_embeddings = pd.read_csv(f'{dataset}nonphishing_nft_embeddings.csv')
nft_labels = pd.read_csv(f'{dataset}nonphishing_nft_labels.csv')
hack_embeddings = pd.read_csv(f'{dataset}nonphishing_hack_embeddings.csv')
hack_labels = pd.read_csv(f'{dataset}nonphishing_hack_labels.csv')

nonphishing_embeddings = pd.concat([nft_embeddings, hack_embeddings], ignore_index=True)
nonphishing_labels = pd.concat([nft_labels, hack_labels], ignore_index=True)
nonphishing_labels = nonphishing_labels['label'].tolist()

# 划分embeddings
phishing_train_embeddings, phishing_test_embeddings, phishing_train_labels, phishing_test_labels = train_test_split(
    phishing_embeddings, phishing_labels, test_size=0.2, random_state=42
)

nonphishing_train_embeddings, nonphishing_test_embeddings, nonphishing_train_labels, nonphishing_test_labels = train_test_split(
    nonphishing_embeddings, nonphishing_labels, test_size=0.2, random_state=42
)

# 构建训练集和测试集
train_embeddings = pd.concat([phishing_train_embeddings, nonphishing_train_embeddings], ignore_index=True)
train_labels = phishing_train_labels + nonphishing_train_labels
dtrain = xgb.DMatrix(train_embeddings, label=train_labels)

test_embeddings = pd.concat([phishing_test_embeddings, nonphishing_test_embeddings], ignore_index=True)
test_labels = phishing_test_labels + nonphishing_test_labels
dtest = xgb.DMatrix(test_embeddings)

print("Phishing Embeddings Shape:", phishing_embeddings.shape)
print("Non-Phishing Embeddings Shape:", nonphishing_embeddings.shape)
print("Train Shape:", train_embeddings.shape)
print("Test Shape:", test_embeddings.shape)

# 设置参数并训练模型
params = {
    'objective': 'multi:softmax',  # 分类任务
    'num_class': 2,  # 类别数
    'max_depth': 3,
    'eta': 0.1,
}
model = xgb.train(params, dtrain, num_boost_round=100)

# 预测
preds = model.predict(dtest)

# 计算准确率
accuracy = accuracy_score(test_labels, preds)
print(f"Accuracy: {accuracy:.2f}")

# 计算召回率和其他指标
report = classification_report(test_labels, preds, target_names=['phishing', 'nonphishing'])
print("Classification Report:")
print(report)
