import pandas as pd

rawDF = pd.read_csv("data/exoplanet_data.csv", comment="#") # Reading data without comments.

rawDF = rawDF.dropna() # Dropping all NAs for clean data.

rawDF = rawDF.drop("st_teff", axis=1) # Decided to drop host's values.
rawDF = rawDF.drop("st_rad", axis=1)
rawDF = rawDF.drop("st_mass", axis=1)
rawDF = rawDF.drop("st_lum", axis=1)

rawDF = rawDF[rawDF['pl_orbsmax'] <= 1.5] # Planet to host distance set to less than 1.5 AU
rawDF = rawDF[rawDF['pl_rade'] <= 20] # Planet radius set to less than 20 Earth radii
rawDF = rawDF[rawDF['pl_bmasse'] <= 1000] # Planet mass set to less than 1000 Earth masses
rawDF = rawDF[rawDF['pl_dens'] <= 30] # Planet density set to less than 30 g/cm^3
rawDF = rawDF[rawDF['pl_orbeccen'] >= 0] # Planet orbital eccentricity set to greater than 0
cleanDF = rawDF[rawDF['pl_insol'] <= 4000] # Planet insolation flux set to less than 4000 Earth flux
# Planet equilibrium temperature data already clean
# Planet distance from Earth already clean

cleanDF.to_csv("data/processed_data.csv", index=False) # Exporting clean data.