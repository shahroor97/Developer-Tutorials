
### imports first
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

            #1) first we load the data sets

data = fetch_california_housing(as_frame=True)
df = data.frame
target = "MedHouseVal"
df.to_csv("california_housing.csv", index=False)
print("\nSaved dataset as california_housing.csv")

            #2) Have a look and quick peek (tabular format)

print("\nShape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nHead:\n", df.head())
print("\nSummary stats:\n", df.describe())

            ##3) check out and save two simple plots, thsi will generate two files and graphs in png 
plt.figure()
df[target].hist(bins=40)
plt.title("Target distribution: MedHouseVal")
plt.xlabel("Median House Value (100k USD)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("hist_medhouseval.png")

plt.figure()
plt.scatter(df["MedInc"], df[target], s=8)
plt.title("Income vs Median House Values")
plt.xlabel("MedInc (median income in 10k USD)")
plt.ylabel("MedHouseVal (100k USD)")
plt.tight_layout()
plt.savefig("scatter_medinc_target.png")

print("\nSaved plots: hist_medhouseval.png, scatter_medinc_target.png")

##SO FAR ABOVE WE ARE JUST CHECKING THE DATA AND PARSING THROUGH IT TO LEARN WHATS THERE

            ###4) train/test split + model training

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

##split into x and y, then into 80% for learning and 20% for testing
X = df.drop(columns=[target])
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
##Train the linearregression model
model = LinearRegression()
model.fit(X_train, y_train)

##evaluate on test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nModel performance:")
print(f" Mean Squared ErrorL {mse:.3f}")
print(f" R2 Score: {r2:.3f}")

            ##5) visualise predicted vs actual values
plt.figure()
plt.scatter(y_test, y_pred, s=8)
plt.title("Predicted vs Actual House Values")
plt.xlabel("Actual (True) Values")
plt.ylabel("Predicated Values")

###add prediction line for reference
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], "r--", linewidth=2)

plt.tight_layout()
plt.savefig("pred_vs_actual.png")
print("\nSaved plot: pred_vs_actual.png")


            ##6) Check feature importance (coeffecients)
importance = pd.Series(model.coef_, index=X.columns).sort_values(key=abs, ascending=False)

print("\nFeature importance (by absolute coefficient value):")
print(importance)

#plot
plt.figure()
importance.plot(kind="bar")
plt.title("Feature importance (linear regression coeffecients)")
plt.ylabel("Coefficient value")
plt.tight_layout()
plt.savefig("feature_importance.png")
print("\nSaved plot: feature_importance.png")

###7) visualise data geographically
plt.figure(figsize=(8,6))
plt.scatter(
    df["Longitude"],
    df["Latitude"],
    c=df["MedHouseVal"],
    cmap="plasma",
    s=10,
    alpha=0.6
)
plt.colorbar(label="Median House Value (100k USD)")
plt.title("California Housing Prices by Location")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.savefig("california_map.png")
print("\nSaved plot: california_map.png")

##8) another plot same at 7, but dot size depends on population density
plt.figure(figsize=(8, 6))
plt.scatter(
    df["Longitude"],
    df["Latitude"],
    c=df["MedHouseVal"],      # color by house value
    s=df["Population"] / 50, # size by population (scaled down)
    cmap="viridis",
    alpha=0.5
)
plt.colorbar(label="Median House Value (100k USD)")
plt.title("California Housing Prices and Population Density")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.savefig("california_map_population.png")
print("\nSaved plot: california_map_population.png")