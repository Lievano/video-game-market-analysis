"""Data preparation utilities for the video game market analysis project."""

from __future__ import annotations

import pandas as pd

REGIONAL_SALES_COLUMNS = ["na_sales", "eu_sales", "jp_sales", "other_sales"]


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the dataframe with normalized snake-case lowercase columns."""
    clean = df.copy()
    clean.columns = clean.columns.str.strip().str.lower()
    return clean


def preprocess_games(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare raw video game sales data for market analysis.

    The function performs conservative cleaning:
    - standardizes column names
    - removes rows without game name or genre
    - converts year and score fields to numeric
    - treats 'tbd' user scores as missing
    - preserves missing critic/user scores instead of fabricating review signal
    - fills missing ratings as 'Unknown'
    - adds global_sales as the sum of regional sales
    """
    games = standardize_columns(df)
    games = games.dropna(subset=["name", "genre"]).reset_index(drop=True)

    games["year_of_release"] = pd.to_numeric(games["year_of_release"], errors="coerce").astype("Int64")
    games["critic_score"] = pd.to_numeric(games["critic_score"], errors="coerce")
    games["user_score"] = pd.to_numeric(games["user_score"], errors="coerce")
    games["rating"] = games["rating"].fillna("Unknown")

    games["global_sales"] = games[REGIONAL_SALES_COLUMNS].sum(axis=1)
    return games


def filter_relevant_period(df: pd.DataFrame, start_year: int = 2012, end_year: int = 2016) -> pd.DataFrame:
    """Filter the market window used for forward-looking campaign planning."""
    return df[df["year_of_release"].between(start_year, end_year)].copy()
