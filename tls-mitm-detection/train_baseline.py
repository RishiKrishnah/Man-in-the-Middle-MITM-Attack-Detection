import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv("tls_features.csv")

X = df[[
    "packet_length",
    "cert_length"
]]

model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

joblib.dump(model, "tls_baseline_model.pkl")
print("Baseline TLS behavior model trained and saved.")
