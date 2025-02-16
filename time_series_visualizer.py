import pandas as pd
import matplotlib.pyplot as plt

# Veriyi yükle
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Aykırı verileri filtrele
lower_bound = df["value"].quantile(0.025)
upper_bound = df["value"].quantile(0.975)
df_clean = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df_clean.index, df_clean["value"], color="red", linewidth=1)

    # Grafik Başlık ve Etiketler
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Kaydet ve Göster
    plt.savefig("line_plot.png")
    plt.show()
