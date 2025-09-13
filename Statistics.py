import pandas as pd
import numpy as np

DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
feature_groups = ["mean", "se", "worst"]
base_features = ["radius", "texture", "perimeter", "area", "smoothness",
"compactness", "concavity", "concave_points", "symmetry", "fractal_dimension"]

feature_cols = [f"{b}_{g}" for g in feature_groups for b in base_features]
cols = ["id", "diagnosis"] + feature_cols
df = pd.read_csv(DATA_URL, header=None, names=cols)
print(df.head(5))

median_radius = np.median(df["radius_mean"])
median_texture = np.median(df["texture_mean"])
median_area = np.median(df["area_mean"])
avg_radius = np.mean(df["radius_mean"])
avg_texture = np.mean(df["texture_mean"])
avg_area = np.mean(df["area_mean"])
desv_pad_radius = np.std(df["radius_mean"])
desv_pad_texture = np.std(df["texture_mean"])
desv_pad_area = np.std(df["area_mean"])

print(f"Mediana de radius_mean: {median_radius:.2f}")
print(f"Mediana de texture_mean: {median_texture:.2f}")
print(f"Mediana de area_mean: {median_area:.2f}")
print(f"Média de radius_mean: {avg_radius:.2f}")
print(f"Média de texture_mean: {avg_texture:.2f}")
print(f"Média de area_mean: {avg_area:.2f}")
print(f"Desvio padrão de radius_mean: {desv_pad_radius:.2f}")
print(f"Desvio padrão de texture_mean: {desv_pad_texture:.2f}")
print(f"Desvio padrão de area_mean: {desv_pad_area:.2f}")

Q1_radius= np.percentile(df["radius_mean"], 25)
Q1_texture= np.percentile(df["texture_mean"], 25)
Q1_area= np.percentile(df["area_mean"], 25)
Q3_radius= np.percentile(df["radius_mean"], 75)
Q3_texture= np.percentile(df["texture_mean"], 75)
Q3_area= np.percentile(df["area_mean"], 75)
IQR_radius = Q3_radius - Q1_radius
IQR_texture = Q3_texture - Q1_texture
IQR_area = Q3_area - Q1_area

print(f"Quartil 1 de radius_mean: {Q1_radius:.2f}")
print(f"Quartil 2 de radius_mean: {median_radius:.2f}")
print(f"Quartil 3 de radius_mean: {Q3_radius:.2f}")
print(f"IQR de radius_mean: {IQR_radius:.2f}")
print(f"Quartil 1 de texture_mean: {Q1_texture:.2f}")
print(f"Quartil 2 de texture_mean: {median_texture:.2f}")
print(f"Quartil 3 de texture_mean: {Q3_texture:.2f}")
print(f"IQR de texture_mean: {IQR_texture:.2f}")
print(f"Quartil 1 de area_mean: {Q1_radius:.2f}")
print(f"Quartil 2 de area_mean: {median_area:.2f}")
print(f"Quartil 3 de area_mean: {Q3_radius:.2f}")
print(f"IQR de area_mean: {IQR_radius:.2f}")

avg_radius_ben = np.mean(df[df["diagnosis"] == "B"]["radius_mean"])
print(f"Média de radius_mean benigna: {avg_radius_ben:.2f}")
avg_radius_mal = np.mean(df[df["diagnosis"] == "M"]["radius_mean"])
print(f"Média de radius_mean maligna: {avg_radius_mal:.2f}")

avg_area_ben = np.mean(df[df["diagnosis"] == "B"]["area_worst"])
print(f"Média de area_worst benigna: {avg_area_ben:.2f}")
avg_area_mal = np.mean(df[df["diagnosis"] == "M"]["area_worst"])
print(f"Média de area_worst maligna: {avg_area_mal:.2f}")

ben_per_cent= df["diagnosis"].value_counts(normalize=True)["B"] * 100
mal_per_cent= df["diagnosis"].value_counts(normalize=True)["M"] * 100
print("Os valores absolutos de diagnósticos benignos são: ", df["diagnosis"].value_counts()["B"], " e o de malignos são: ", df["diagnosis"].value_counts()["M"])
print(f"As proporções entre diagnósticos benignos é de : {ben_per_cent:.2f}% e a de malignos é de: {mal_per_cent:.2f}%")
table = pd.DataFrame({"n": df["diagnosis"].value_counts(), "%": df["diagnosis"].value_counts(normalize=True) * 100})
print(table)


corr_raius_perimeter = df["radius_mean"].corr(df["perimeter_mean"])
print(f"A correlação entre radius_mean e perimeter_mean é de : {corr_raius_perimeter:.3f}")

df["diagnosis_num"] = df["diagnosis"].map({"B": 1, "M": 0})
correlations = df.corr(numeric_only=True)["diagnosis_num"].drop("diagnosis_num")
top3 = correlations.abs().sort_values(ascending=False).head(3)
print("As três variáveis mais correlacionadas com o diagnóstico são: ", top3.index.tolist())

top10 = df.nlargest(10, "radius_worst")[["diagnosis", "radius_worst", "area_worst"]]
print("Os 10 casos com os maiores radius_worst são:")
print(top10)