from sklearn.datasets import load_breast_cancer
import pandas as pd

            ##1)Load data
data = load_breast_cancer(as_frame=True)
df = data.frame
df.to_csv("data.csv", index=False)
print(df.head())
print(df['target'].value_counts())

            ##2) Clean and preprocess
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
##set x and y variables
X=df.drop(columns=['target'])
y=df['target']
##set train and test data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
##set scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

##3) Train both Logistic Regression and Decision Tree for comparison

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
##Logistical Regression
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train, y_train)
#Decision Tree
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

print("Training Complete.")

##4) calculate accuracy, percision, recall and F1 for both models
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
y_pred_log = log_reg.predict(X_test)
y_pred_tree = tree.predict(X_test)

# Metrics for Logistic Regression
print("Logistic Regression:")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print("Precision:", precision_score(y_test, y_pred_log))
print("Recall:", recall_score(y_test, y_pred_log))
print("F1 Score:", f1_score(y_test, y_pred_log))

# Metrics for Decision Tree
print("\nDecision Tree:")
print("Accuracy:", accuracy_score(y_test, y_pred_tree))
print("Precision:", precision_score(y_test, y_pred_tree))
print("Recall:", recall_score(y_test, y_pred_tree))
print("F1 Score:", f1_score(y_test, y_pred_tree))

##5) Comparing and visualising scores

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, f1_score

# Logistic Regression Confusion Matrix
disp_log = ConfusionMatrixDisplay.from_estimator(log_reg, X_test, y_test)
disp_log.ax_.set_title("Logistic Regression - Confusion Matrix")
plt.savefig("logreg_confusion_matrix.png", bbox_inches='tight', dpi=300)
plt.close()

# Decision Tree Confusion Matrix
disp_tree = ConfusionMatrixDisplay.from_estimator(tree, X_test, y_test)
disp_tree.ax_.set_title("Decision Tree - Confusion Matrix")
plt.savefig("tree_confusion_matrix.png", bbox_inches='tight', dpi=300)
plt.close()

# Bar chart comparison
models = ['LogReg', 'DecisionTree']
accuracies = [
    accuracy_score(y_test, log_reg.predict(X_test)),
    accuracy_score(y_test, tree.predict(X_test))
]
f1_scores = [
    f1_score(y_test, log_reg.predict(X_test)),
    f1_score(y_test, tree.predict(X_test))
]

plt.bar(models, accuracies, alpha=0.7, label='Accuracy')
plt.bar(models, f1_scores, alpha=0.7, label='F1 Score')
plt.ylabel('Score')
plt.title('Model Performance Comparison')
plt.legend()
plt.savefig("model_comparison.png", bbox_inches='tight', dpi=300)
plt.close()