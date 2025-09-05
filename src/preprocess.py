import pandas as pd

rawDF = pd.read_csv("data/exoplanet_data.csv", comment="#")

cleanDF = rawDF.dropna()

cleanDF = cleanDF[cleanDF['pl_orbsmax'] <= 1.5] # Planet to host distance set to less than 1.5 AU
cleanDF = cleanDF[cleanDF['pl_rade'] <= 20] # Planet radius set to less than 20 Earth radii
cleanDF = cleanDF[cleanDF['pl_bmasse'] <= 1000] # Planet mass set to less than 1000 Earth masses
cleanDF = cleanDF[cleanDF['pl_dens'] <= 30] # Planet density set to less than 30 g/cm^3
cleanDF = cleanDF[cleanDF['pl_orbeccen'] >= 0] # Planet orbital eccentricity set to greater than 0

cleanDF.to_csv("data/processed_data.csv", index=False)