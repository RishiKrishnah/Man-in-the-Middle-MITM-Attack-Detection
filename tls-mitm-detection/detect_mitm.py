import pandas as pd
import joblib

model = joblib.load("tls_baseline_model.pkl")
df = pd.read_csv("tls_features.csv")

X = df[[
    "packet_length",
    "cert_length"
]]

df["anomaly"] = model.predict(X)

df["anomaly"] = df["anomaly"].map({
    1: "Normal",
    -1: "MITM Suspected"
})

print(df["anomaly"].value_counts())
df.to_csv("mitm_detection_results.csv", index=False)

print("MITM detection completed.")
