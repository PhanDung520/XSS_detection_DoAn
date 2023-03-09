import pandas as pd
from sklearn.model_selection import train_test_split
import _pickle as cPickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# lấy ra các đặc trưng
Script = pd.read_csv(r'')

# Biểu diễn dữ liệu dưới dạng 1 dataFrame
df = pd.DataFrame(Script, columns=['hasLt', 'hasScript', 'hasAlert', 'hasBigSmallSign2', 'hasBigSmallSign1', 'hasAnd',
                                   'hasPercentage', 'hasSlash', 'hasBackSlash', 'hasPlus', 'hasDocument', 'hasWindow',
                                   'hasOnload', 'hasOnError', 'hasDiv', 'hasIframe', 'hasImg', 'hasSRC', 'hasVar',
                                   'hasEval', 'hasHref', 'hasCookie', 'hasStringfromCharCode', 'hasSingleQoute',
                                   'hasQuestionMark', 'hasExclamationMark', 'hasSemicolon', 'hasHTTP', 'hasJS',
                                   'hasHash', 'hasEqual', 'hasOpenBracket', 'hasCloseBracket', 'hasDoubleBracket',
                                   'hasDollar', 'hasOpenParenthesis', 'hasCloseParenthesis', 'hasAsterisk', 'hasComma',
                                   'hasHyphen', 'hasLessThan', 'hasGreaterThan', 'hasAt', 'hasUnderscore',
                                   'hasLocation', 'hasSearch', 'hasAndHash', 'hasColon', 'hasDots', 'hasOpenBrace',
                                   'hasCloseBrace', 'hasTilde', 'hasSpace', 'hasGrave', 'hasDoubleEquals',
                                   'hasDoubleSlash', 'hasVerticalBar', 'hasPower', 'LettersRatio', 'NumbuersRatio',
                                   'SymbolsRatio'])

X = df['hasLt', 'hasScript', 'hasAlert', 'hasBigSmallSign2', 'hasBigSmallSign1', 'hasAnd',
'hasPercentage', 'hasSlash', 'hasBackSlash', 'hasPlus', 'hasDocument', 'hasWindow',
'hasOnload', 'hasOnError', 'hasDiv', 'hasIframe', 'hasImg', 'hasSRC', 'hasVar',
'hasEval', 'hasHref', 'hasCookie', 'hasStringfromCharCode', 'hasSingleQoute',
'hasQuestionMark', 'hasExclamationMark', 'hasSemicolon', 'hasHTTP', 'hasJS',
'hasHash', 'hasEqual', 'hasOpenBracket', 'hasCloseBracket', 'hasDoubleBracket',
'hasDollar', 'hasOpenParenthesis', 'hasCloseParenthesis', 'hasAsterisk', 'hasComma',
'hasHyphen', 'hasLessThan', 'hasGreaterThan', 'hasAt', 'hasUnderscore',
'hasLocation', 'hasSearch', 'hasAndHash', 'hasColon', 'hasDots', 'hasOpenBrace',
'hasCloseBrace', 'hasTilde', 'hasSpace', 'hasGrave', 'hasDoubleEquals',
'hasDoubleSlash', 'hasVerticalBar', 'hasPower', 'LettersRatio', 'NumbuersRatio',
'SymbolsRatio']

y = df['Class']

# Chia dữ liệu thành 2 tập huấn luyện. Tập huấn luyện chiếm 80% và tập test chiếm 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

clf = RandomForestClassifier(n_estimators=40)  # - So cay: 40 cay
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
with open(r'', 'wb') as f:
    cPickle.dump(clf, f)
