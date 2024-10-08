# -*- coding: utf-8 -*-
"""Métricas de Avaliação de Aprendizado.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gu-9aqLqOsawacUq5AJ9WbCh0Z7l9TEZ
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay


X, y = make_classification(n_samples=10_000, weights=[0.9, 0.1], random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

classifier_05 = LogisticRegression(C=1e6, random_state=0).fit(X_train, y_train)
_ = ConfusionMatrixDisplay.from_estimator(classifier_05, X_test, y_test)

vp = 2200
vn = 69
fp = 182
fn = 49

sencibilidade = vp / (vp + fn)
especificidade = vn/ (fp + vn)
acurácia = (vp + vn) / (vp + fn + vn + fp)
precisão = vp / (vp + fp)
f_score = 2 * (precisão * sencibilidade) / (precisão + sencibilidade)

print(sencibilidade)
print(especificidade)
print(acurácia)
print(precisão)
print(f_score)