import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Veriyi yükle
df = pd.read_csv("medical_examination.csv")

# Fazla kilolu olanları belirleme
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Normalizasyon
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Kategorik Plot Çizimi
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    fig = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind="count")
    fig.savefig("catplot.png")
    return fig

# Isı Haritası Çizimi
def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", ax=ax)
    
    fig.savefig("heatmap.png")
    return fig
