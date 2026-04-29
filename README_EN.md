# Video Game Market Analysis

## Executive Summary

This project analyzes historical video game sales to identify patterns that can support campaign planning and market prioritization. It is framed as a strategic market intelligence system, not as a simple exploratory notebook.

The analysis studies platform lifecycle dynamics, genre profitability, regional differences, review-score relationships, and statistical hypotheses about user ratings.

## Business Problem

An online video game retailer needs to identify promising platforms, genres, and regional market patterns to plan future advertising campaigns.

The central question is:

> Which market signals help identify games and segments with stronger commercial potential?

## Technical Objective

The objective is to clean, analyze, and interpret historical game sales data using reproducible Python workflows. The analysis focuses on:

- platform sales evolution
- recent platform momentum
- global and regional sales patterns
- genre performance
- relationship between review scores and sales
- formal hypothesis testing on user scores

## Dataset

The dataset contains video game records with fields such as:

| Column | Meaning |
|---|---|
| `Name` | Game title |
| `Platform` | Console or gaming platform |
| `Year_of_Release` | Release year |
| `Genre` | Game genre |
| `NA_sales` | North America sales, in millions |
| `EU_sales` | Europe sales, in millions |
| `JP_sales` | Japan sales, in millions |
| `Other_sales` | Other-region sales, in millions |
| `Critic_Score` | Critic score out of 100 |
| `User_Score` | User score out of 10 |
| `Rating` | ESRB content rating |

## Methodology

### 1. Data Preparation

The pipeline normalizes column names, converts year and score columns to numeric types, handles `tbd` user scores as missing values, fills missing ESRB ratings as `Unknown`, and computes `global_sales` as the sum of regional sales.

### 2. Platform Lifecycle Analysis

The project estimates how platforms rise, peak, and decline over time. This helps separate obsolete platforms from platforms that may still support future campaign planning.

### 3. Market Window Selection

A recent window is used to make the analysis more relevant for forward-looking decisions. Older historical data is useful for lifecycle context, but recent years carry more campaign value.

### 4. Genre and Platform Performance

The analysis compares sales by platform and genre to identify higher-impact segments.

### 5. Regional Profiles

North America, Europe, and Japan are profiled separately by top platforms, genres, and ESRB ratings. This shows where global strategy should be localized.

### 6. Review Signal Analysis

The project checks correlations between critic/user scores and sales for selected platforms. Critic scores usually show stronger association with sales than user scores.

### 7. Hypothesis Testing

Two independent group comparisons are tested:

1. Mean user scores for Xbox One and PC.
2. Mean user scores for Action and Sports games.

Levene's test is used to assess variance equality before applying the independent t-test.

## Results

Main findings:

- Platform lifecycle matters: past dominance does not guarantee future relevance.
- Recent-generation platforms are more useful for campaign planning than legacy platforms.
- Genre performance is not uniform across regions.
- Japan differs substantially from North America and Europe in platform and genre preferences.
- Critic scores tend to be more commercially informative than user scores.
- Hypothesis testing adds statistical discipline beyond visual comparison.

## Impact

This project can support:

- campaign targeting
- inventory planning
- market-entry prioritization
- platform/genre focus decisions
- regional marketing strategy

## Repository Structure

```text
video-game-market-analysis/
├── data/
│   └── games.csv
├── notebooks/
│   ├── project_EN.ipynb
│   └── project_ES.ipynb
├── src/
│   ├── preprocessing.py
│   ├── analysis.py
│   └── hypothesis.py
├── reports/
│   └── figures/
├── README.md
├── README_EN.md
├── README_ES.md
├── docs/
├── requirements.txt
└── .gitignore
```

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/project_EN.ipynb
```

## Next Steps

- Add predictive modeling for expected sales tier.
- Add dashboard views for platform and genre comparison.
- Incorporate more recent market data.
- Add publisher/developer features if available.
- Extend hypothesis testing with non-parametric alternatives.
