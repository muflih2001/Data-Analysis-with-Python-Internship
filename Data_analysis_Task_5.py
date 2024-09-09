# -*- coding: utf-8 -*-
"""Task - 5 Data Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t6yBe7aDfWDfWJaLYfONOyXDoo25Lw5G
"""

import pandas as pd
data = pd.read_csv('heart.csv')

print(data.head())

print(data.info())

data.describe()

data['age_group'] = pd.cut(data['age'], bins=[0, 40, 50, 60, 100], labels=['<40', '40-50', '50-60', '60+'])

data['chol_category'] = pd.cut(data['chol'], bins=[0, 200, 239, 1000], labels=['normal', 'borderline', 'high'])

data['age_chol'] = data['age'] * data['chol']
data['thalach_age'] = data['thalachh'] * data['age']

print(data.head())

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

features = data.drop(columns=['output', 'age_group', 'chol_category'])

features = pd.get_dummies(features, drop_first=True)

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

pca = PCA(n_components=0.95)  # retain 95% of the variance
features_pca = pca.fit_transform(features_scaled)

explained_variance = pca.explained_variance_ratio_
n_components = pca.n_components_

print(features_pca.shape)

print(explained_variance)

print(n_components)

from sklearn.ensemble import RandomForestClassifier

X = pd.get_dummies(data.drop(columns=['output', 'age_group', 'chol_category']), drop_first=True)
y = data['output']

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

feature_importances = rf_model.feature_importances_
important_features = pd.Series(feature_importances, index=X.columns).sort_values(ascending=False)

print(important_features.head(15))

top_features = important_features.head(15).index
X_top = X[top_features]

rf_model_top = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model_top.fit(X_top, y)

from sklearn.model_selection import cross_val_score
scores = cross_val_score(rf_model_top, X_top, y, cv=5)
print(f'Cross-validated scores: {scores}')
print(f'Mean score: {scores.mean()}')
