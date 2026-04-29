"""Reusable analysis helpers for platform, genre, and regional market structure."""

from __future__ import annotations

import pandas as pd

REGION_LABELS = {
    "na_sales": "North America",
    "eu_sales": "Europe",
    "jp_sales": "Japan",
}


def annual_release_counts(df: pd.DataFrame) -> pd.DataFrame:
    """Count game releases by year."""
    return (
        df.dropna(subset=["year_of_release"])
        .groupby("year_of_release")
        .size()
        .rename("games_released")
        .reset_index()
    )


def platform_sales(df: pd.DataFrame, sales_col: str = "global_sales") -> pd.DataFrame:
    """Rank platforms by total sales."""
    return (
        df.groupby("platform", as_index=False)[sales_col]
        .sum()
        .sort_values(sales_col, ascending=False)
        .reset_index(drop=True)
    )


def platform_lifecycle(df: pd.DataFrame) -> pd.DataFrame:
    """Estimate active window, peak year, rise time, and decline time for each platform."""
    yearly = df.groupby(["platform", "year_of_release"], as_index=False)["global_sales"].sum()
    idx = yearly.groupby("platform")["global_sales"].idxmax()
    peaks = yearly.loc[idx, ["platform", "year_of_release", "global_sales"]].rename(
        columns={"year_of_release": "peak_year", "global_sales": "peak_sales"}
    )
    ranges = df.groupby("platform")["year_of_release"].agg(first_year="min", last_year="max").reset_index()
    out = ranges.merge(peaks, on="platform", how="left")
    out["active_years"] = out["last_year"] - out["first_year"] + 1
    out["rise_time"] = out["peak_year"] - out["first_year"]
    out["decline_time"] = out["last_year"] - out["peak_year"]
    return out.sort_values("peak_sales", ascending=False).reset_index(drop=True)


def genre_sales(df: pd.DataFrame, sales_col: str = "global_sales") -> pd.DataFrame:
    """Rank genres by total sales."""
    return (
        df.groupby("genre", as_index=False)[sales_col]
        .sum()
        .sort_values(sales_col, ascending=False)
        .reset_index(drop=True)
    )


def review_sales_correlation(df: pd.DataFrame, platform: str) -> pd.Series:
    """Return correlation between review scores and global sales for one platform."""
    subset = df[df["platform"] == platform]
    return subset[["critic_score", "user_score", "global_sales"]].corr()["global_sales"].drop("global_sales")


def regional_top(df: pd.DataFrame, region_col: str, dimension: str, top_n: int = 5) -> pd.DataFrame:
    """Calculate top-N platforms or genres by region with market share."""
    total = df[region_col].sum()
    out = (
        df.groupby(dimension, as_index=False)[region_col]
        .sum()
        .sort_values(region_col, ascending=False)
        .head(top_n)
        .reset_index(drop=True)
    )
    out["market_share"] = out[region_col] / total if total else 0
    return out
