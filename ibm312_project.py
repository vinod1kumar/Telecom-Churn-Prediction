# -*- coding: utf-8 -*-
"""IBM312_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12rtkbCc3cZy0N8YPs6FRJaCWpvTWVIRT
"""

# Importing and pre-processing data

data = pd.read_csv('train.csv')

# Dropping irrelevant features

useless_features = ['state', 'area_code']
data.drop(useless_features, axis = 1, inplace= True)

x = data.drop('churn', axis = 1)
y = data['churn']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Handling string data - 'yes'/'no'

dict = {'yes' : 1, 'no' : 0}

x_train['international_plan'] = x_train['international_plan'].replace(dict)
x_train['voice_mail_plan'] = x_train['voice_mail_plan'].replace(dict)

x_test['international_plan'] = x_test['international_plan'].replace(dict)
x_test['voice_mail_plan'] = x_test['voice_mail_plan'].replace(dict)

# Training PCA model to reduce the dimensions by 3 times

pca = PCA(n_components = 5)
pca.fit(x_train)

# Importing libraries

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
from sklearn.metrics import precision_recall_curve

# Transforming the training and testing data

x_train_reduced = pca.transform(x_train)
x_test_reduced = pca.transform(x_test)

# Training logistic regression model

model = LogisticRegression(max_iter=10000)
model.fit(x_train, y_train)

# Indicating importance of individual features in classification

model_fi = permutation_importance(model, x_train, y_train)
model_fi['importances_mean']

from sklearn.utils.multiclass import type_of_target
#Testing the logistic regression model
pred = model.predict(x_test)
print("Confusion Matrix : ")
print(confusion_matrix(pred, y_test))
print("Accuracy : ", accuracy_score(pred, y_test))
y_test=np.array(y_test)
y_test_binary=[]
y_pred_binary=[]
for i in range(len(y_test)):
 if(y_test[i]=='no'):
   y_test_binary.append(0)
 else:
    y_test_binary.append(1)
 if(pred[i]=='no'):
   y_pred_binary.append(0)
 else:
    y_pred_binary.append(1)

#precision-recall curve for test data

precision, recall, thresholds = precision_recall_curve(y_test_binary, y_pred_binary)
plt.fill_between(recall, precision)
plt.ylabel("Precision")
plt.xlabel("Recall")
plt.title("Train Precision-Recall curve");



