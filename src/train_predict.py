import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

exoplanetDF = pd.read_csv("data/scored_exoplanets.csv")
features = ["pl_rade", "pl_bmasse", "pl_dens", "pl_orbeccen", "pl_insol", "pl_eqt"]

x = exoplanetDF[features]
y = exoplanetDF["score"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=67)

rf = RandomForestRegressor(n_estimators=200, max_depth=8, random_state=67)

rf.fit(x_train, y_train)

y_pred = rf.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, color='blue', edgecolor='black', alpha=0.5)
plt.plot([0, 100], [0, 100], color='red', linestyle='--')
plt.xlabel('Actual Habitability Score')
plt.ylabel('Predicted Habitability Score')
plt.title('Predicted vs Actual Habitability Scores')
plt.grid(True)
plt.tight_layout()

plt.savefig('results/predicted_vs_actual.png')
plt.show()