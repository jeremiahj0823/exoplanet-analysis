import pandas as pd

rawDF = pd.read_csv("data/exoplanet_data.csv", comment="#")
cleanDF = rawDF.dropna()
cleanDF.to_csv("data/processed_data.csv", index=False)