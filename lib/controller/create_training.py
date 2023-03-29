from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import lib.model.utils as utils
import _pickle as cPickle

# Đọc dữ liệu từ tệp
data = pd.read_csv(utils.training_dataset_file_name)

# Chuyển đổi dữ liệu thành mảng NumPy
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Tạo một bộ phân loại random forest
clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)

# Huấn luyện bộ phân loại
clf.fit(X, y)

# lưu model
with open(utils.training_model_file_name, 'wb') as f:
    cPickle.dump(clf, f)











