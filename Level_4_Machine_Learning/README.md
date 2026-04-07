# 🤖 Level 4 — Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Duration-3--4%20Months-ef4444?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Difficulty-Intermediate--Advanced-ef4444?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Prerequisites-Level%203-f59e0b?style=for-the-badge" />
</p>

> **This is the core of Data Science.** Learn to build, evaluate, and deploy ML models that solve real problems.

---

## 📚 What You'll Learn

| Module | Topics | Folder |
|---|---|---|
| 🔄 ML Lifecycle | Problem framing, data collection, EDA, model selection, deployment, monitoring | [`01_ML_Lifecycle/`](01_ML_Lifecycle/) |
| 📈 Supervised | Linear/Logistic regression, decision trees, Random Forest, XGBoost, SVM, KNN | [`02_Supervised_Learning/`](02_Supervised_Learning/) |
| 🔍 Unsupervised | K-Means, DBSCAN, PCA, t-SNE, anomaly detection, association rules | [`03_Unsupervised_Learning/`](03_Unsupervised_Learning/) |
| 🎮 Reinforcement | Q-Learning, DQN, policy gradient, MDP, exploration vs exploitation | [`04_Reinforcement_Learning/`](04_Reinforcement_Learning/) |
| 📏 Evaluation | Classification/regression metrics, bias-variance tradeoff, cross-validation | [`05_Model_Evaluation/`](05_Model_Evaluation/) |

---

## 🎯 Learning Objectives

- [ ] Understand the end-to-end ML lifecycle
- [ ] Implement and compare multiple supervised learning algorithms
- [ ] Perform clustering and dimensionality reduction
- [ ] Evaluate models with proper metrics and cross-validation
- [ ] Tune hyperparameters with Grid Search, Random Search, and Optuna
- [ ] Deploy a model with Flask/FastAPI

---

## 🛠️ Key Libraries

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
import optuna
import mlflow
```

---

## ➡️ Next Level

After mastering ML fundamentals, move to **[Level 5 — Applied Data Science](../Level_5_Applied_Data_Science/)**.