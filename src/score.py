import pandas as pd

def planet_score(planet):
    score = 0
    temp_score = 0
    rade_score = 0
    masse_score = 0
    dens_score = 0
    eccen_score = 0
    insol_score = 0

    temp = planet["pl_eqt"]
    if 250 <= temp <= 290:
        temp_score = 1
    elif 200 <= temp < 250:
        temp_score = 0.5
    elif 290 < temp <= 340:
        temp_score = 0.5
    else:
        temp_score = 0

    rade = planet["pl_rade"]
    if 0.75 <= rade <= 1.25:
        rade_score = 1
    elif 0.5 <= rade < 0.75:
        rade_score = 0.5
    elif 1.25 < rade <= 2:
        rade_score = 0.5
    else:
        rade_score = 0

    masse = planet["pl_bmasse"]
    if 0.75 <= masse <= 3:
        masse_score = 1
    elif 0.5 <= masse < 0.75:
        masse_score = 0.5
    elif 3 < masse <= 5:
        masse_score = 0.5
    else:
        masse_score = 0

    dens = planet["pl_dens"]
    if 3 <= dens <= 8:
        dens_score = 1
    elif 1 <= dens < 3:
        dens_score = 0.5
    elif 8 < dens <= 10:
        dens_score = 0.5
    else:
        dens_score = 0

    eccen = planet["pl_orbeccen"]
    if 0 <= eccen <= 0.25:
        eccen_score = 1
    elif 0.25 < eccen <= 0.5:
        eccen_score = 0.5
    elif 0.5 < eccen <= 0.75:
        eccen_score = 0.25
    else:
        eccen_score = 0

    insol = planet["pl_insol"]
    if 0.75 <= insol <= 1.25:
        insol_score = 1
    elif 0.5 <= insol < 0.75:
        insol_score = 0.5
    elif 1.25 < insol <= 2:
        insol_score = 0.5
    else:
        insol_score = 0

    score = (0.25*temp_score + 0.15*rade_score + 0.15*masse_score + 0.25*dens_score + 0.1*eccen_score + 0.1*insol_score) * 100
    print(score)
    return score

exoplanetDF = pd.read_csv("data/processed_data.csv")
scores = []
for blank, planet in exoplanetDF.iterrows():
    scores.append(planet_score(planet))

exoplanetDF["score"] = scores

exoplanetDF.to_csv("data/scored_exoplanets.csv", index=False)

planet_scores_df = exoplanetDF[["pl_name", "score"]].sort_values(by="score", ascending=False)
planet_scores_df.to_csv("results/planet_scores.csv", index=False)
