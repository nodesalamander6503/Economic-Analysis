import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from itertools import combinations
#from statsmodels.graphics.tsaplots import plot_acf

def analyze(returns, tag, periods):
    print(returns)

    # 1. Time Series

    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    for ax, item in zip(axes.flatten(), returns.columns):
        ax.plot(returns.index, returns[item], linewidth=0.5)
        ax.set_title(item)
        ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    plt.savefig("figures/" + tag + "-timeseries.png", dpi=150)
    #plt.show()

    # 2. Inter-Item Correlations

    corr = returns.corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", center=0,
                cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
    ax.set_title("Return Correlations")
    plt.tight_layout()
    plt.savefig("figures/" + tag + "-heatmap.png", dpi=150)
    #plt.show()

    # formal hypothesis tests with Bonferroni correction
    n_pairs = len(list(combinations(returns.columns, 2)))
    bonferroni_threshold = 0.05 / n_pairs

    print(f"Bonferroni threshold: p < {bonferroni_threshold:.4f}")
    print()
    for a, b in combinations(returns.columns, 2):
        returns_a = returns[a].dropna()
        returns_b = returns[b].dropna()
        shared = returns_a.index.intersection(returns_b.index)
        r, p = stats.pearsonr(returns_a[shared], returns_b[shared])
        sig = "***" if p < bonferroni_threshold else ""
        print(f"{a:30s} vs {b:30s}: r={r:+.4f}, p={p:.6f} {sig}")

    # 3. Autocorrelation

    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    bonferroni_threshold = 0.05 / (len(returns.columns) * 24)
    for ax, item in zip(axes.flatten(), returns.columns):
        series = returns[item].dropna()
        lags = range(1, 25)
        acf_vals = []
        for lag in lags:
            r, p = stats.pearsonr(series.iloc[:-lag], series.iloc[lag:])
            acf_vals.append(r)
            sig = "***" if p < bonferroni_threshold else ""
            print(f"{item:30s} {lag:>2}: r={r:+4f}, p={p:.6f} {sig}")
        
        # 95% confidence band (approximate)
        conf = 1.96 / np.sqrt(len(series))
        
        ax.bar(lags, acf_vals, width=0.6)
        ax.axhline(y=conf, color='blue', linestyle='--', alpha=bonferroni_threshold)
        ax.axhline(y=-conf, color='blue', linestyle='--', alpha=bonferroni_threshold)
        ax.axhline(y=0, color='black', linewidth=0.5)
        ax.set_title(item)
        ax.set_ylim(-0.3, 0.3)

    plt.tight_layout()
    plt.savefig("figures/" + tag + "-autocorrelation.png", dpi=150)
    #plt.show()

    # 4. Volatility

    cv = returns.std() * np.sqrt(periods * 365)
    print(cv)

    fig, ax = plt.subplots(figsize=(10, 5))
    cv.sort_values().plot(kind="barh", ax=ax)
    ax.set_xlabel("Coefficient of Variation")
    ax.set_title("Volatility by Item")
    #ax.axvline(x=0.01 / (24**0.5), color="red", linestyle="--", label="S&P 500 hourly equiv")
    ax.legend()
    plt.tight_layout()
    plt.savefig("figures/" + tag + "-volatility.png", dpi=150)
    #plt.show()

    # 5. Summary

    summary = pd.DataFrame({
        "mean_price": returns.mean(),
        "std_price": returns.std(),
        "coeff_variation": returns.std() / returns.mean(),
        "min_price": returns.min(),
        "max_price": returns.max(),
        "n_observations": returns.count(),
    })
    print(summary.to_string())

    print()

    print("| Item | Mean Price | Std | CV | Min | Max | N |")
    print("|------|------------|-----|----|-----|-----|---|")
    for item, row in summary.iterrows():
        print(f"| {item} | {row['mean_price']:.2f} | {row['std_price']:.2f} | {row['coeff_variation']:.4f} | {row['min_price']:.2f} | {row['max_price']:.2f} | {int(row['n_observations'])} |")

conn = sqlite3.connect("skyblock-1.db")
df = pd.read_sql("SELECT * FROM prices", conn, parse_dates=["timestamp"])
conn.close()

nice_name_map = {
    "DIAMOND": "Diamond",
    "REDSTONE": "Redstone",
    "MAGIC_MUSHROOM_SOUP": "Magical Mushroom Soup",
    "VIAL_OF_VENOM": "Vial of Venom",
    "SALT_CUBE": "Salt Cube",
    "DIAMONITE": "Diamonite",
    "ESSENCE_WITHER": "Wither Essence",
    "ESSENCE_CRIMSON": "Crimson Essence"
}


df = df.set_index("timestamp")
df = df.sort_index()
df = df.loc["2025-09-20":"2026-03-20"]

wide = df.pivot_table(index=df.index, columns="item", values="buy_price")
hourly = wide.resample("1h").last().dropna(how="all")
hourly.rename(columns=nice_name_map, inplace=True)
returns = hourly.pct_change().dropna()

analyze(returns, "skyblock", 20)
input("press enter to continue")


df = pd.read_csv("yfinance-1.csv", parse_dates=["timestamp"])

df["timestamp"] = pd.to_datetime(df["timestamp"],utc=True)
df = df.set_index("timestamp")
df = df.sort_index()
wide = df.pivot_table(index=df.index, columns="item", values="buy_price")
daily = wide.resample("1D").last().dropna(how="all")
returns = daily.pct_change().dropna()

analyze(returns, "yfinance", 20)



