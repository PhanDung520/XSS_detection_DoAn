from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import lib.model.utils as utils
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
import _pickle as cPickle

# Đọc dữ liệu từ tệp
data = pd.read_csv(utils.training_dataset_file_name_sfs)
# Chuyển đổi dữ liệu thành mảng NumPy
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=26)

# Train the model
model = RandomForestClassifier(n_estimators=40)
model.fit(X_train, y_train)

# Xây dựng mô hình ma trận nhầm lẫn
confusion_matrix = pd.crosstab(y_test, model.predict(X_test), rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)
print(confusion_matrix)

# Tiến hành biểu diễn ma trân nhầm lẫn
y_pred = model.predict(X_test)
print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
plt.show()

# Test the model
# score = model.score(X_test, y_test)
# print(f"Accuracy: {score}")
