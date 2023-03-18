import pandas as pd
from sklearn.model_selection import train_test_split
import _pickle as cPickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import lib.model.utils as utils

# lấy ra các đặc trưng
Script = pd.read_csv(r'C:\Users\phand\OneDrive\Tài liệu\XSS_detection_DoAn\Dataset\final_ds\output_full.csv')

# Biểu diễn dữ liệu dưới dạng 1 dataFrame
df = pd.DataFrame(Script, columns=utils.column_name)

X = df[utils.column_name_without_label]

y = df['Label']

# Chia dữ liệu thành 2 tập huấn luyện. Tập huấn luyện chiếm 80% và tập test chiếm 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=0)

clf = RandomForestClassifier(n_estimators=100)  # - So cay: 40 cay
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Số lần kiểm tra chéo - cross validation(10 folds)
print(np.mean(cross_val_score(clf, X_train, y_train, cv=10)))

# Xây dựng mô hình ma trận nhầm lẫn
confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)
print(confusion_matrix)
# Tiến hành biểu diễn ma trân nhầm lẫn
print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
plt.show()

# lưu model
with open(utils.training_model_file_name, 'wb') as f:
    cPickle.dump(clf, f)
