from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import lib.model.utils as utils
import pandas as pd
import _pickle as cPickle

# Đọc dữ liệu từ tệp
data = pd.read_csv(utils.training_dataset_file_name)
# Chuyển đổi dữ liệu thành mảng NumPy
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=26)

# Train the model
model = RandomForestClassifier(n_estimators=40)
model.fit(X_train, y_train)
# lưu model
with open(utils.training_model_file_name, 'wb') as f:
    cPickle.dump(model, f)
# Test the model
score = model.score(X_test, y_test)
print(f"Accuracy: {score}")