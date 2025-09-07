# Predicting Exoplanet Habitability with Machine Learning

This project uses **NASA Exoplanet Archive** data for determining habitability.

Process:

1. Data was first cleaned to exclude outliers and physical anomalies.

2. Graphs were made using matplotlib to visualize the distribution of planet's features for further cleaning.

3. Exoplanets were then scored based on several factors, including:

*Equilibrium Temperature (K)*: Planets can't be too hot or too cold. Must be in habitable zone.
*Radius (Earth Radii)*: Small planets are likely to not hold an atmosphere. Large planets may be gaseous.
*Mass (Earth Mass)*: Planets too massive may have too high of gravity. Smaller, vice versa.
*Density (g/cm^3)* # Less dense planets are gaseous.
*Insolation Flux (Earth Flux)* # Energy is needed for liquid water.

4. A Random Forest model was trained on actual scores and predicted new scores (80 train / 20 test).



An R^2 score of **0.99** was achieved.

5. Results were all saved to exoplanet-analysis/results.