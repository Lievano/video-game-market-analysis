"""Hypothesis testing helpers for independent group comparisons."""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np
import pandas as pd
from scipy import stats


@dataclass
class TestResult:
    group_a: str
    group_b: str
    n_a: int
    n_b: int
    mean_a: float
    mean_b: float
    levene_pvalue: float
    equal_var: bool
    statistic: float
    pvalue: float
    alpha: float
    reject_null: bool


def compare_user_scores(
    df: pd.DataFrame,
    column: str,
    group_a: str,
    group_b: str,
    alpha: float = 0.05,
) -> TestResult:
    """
    Compare mean user scores between two independent groups using Levene + t-test.

    Welch's t-test is used when Levene's test suggests unequal variance.
    """
    a = df.loc[df[column] == group_a, "user_score"].dropna().astype(float)
    b = df.loc[df[column] == group_b, "user_score"].dropna().astype(float)
    levene = stats.levene(a, b)
    equal_var = bool(levene.pvalue >= alpha)
    test = stats.ttest_ind(a, b, equal_var=equal_var, nan_policy="omit")
    return TestResult(
        group_a=group_a,
        group_b=group_b,
        n_a=int(a.shape[0]),
        n_b=int(b.shape[0]),
        mean_a=float(np.mean(a)),
        mean_b=float(np.mean(b)),
        levene_pvalue=float(levene.pvalue),
        equal_var=equal_var,
        statistic=float(test.statistic),
        pvalue=float(test.pvalue),
        alpha=alpha,
        reject_null=bool(test.pvalue < alpha),
    )
