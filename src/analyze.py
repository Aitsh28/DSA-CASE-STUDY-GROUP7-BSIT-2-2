# src/analyze.py

from typing import List, Dict
import math

# ---------------------------
# BASIC STATS FUNCTIONS
# ---------------------------
def compute_mean(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0

def compute_median(values: List[float]) -> float:
    if not values:
        return 0
    values = sorted(values)
    mid = len(values) // 2
    return (values[mid - 1] + values[mid]) / 2 if len(values) % 2 == 0 else values[mid]

def compute_stddev(values: List[float]) -> float:
    if not values:
        return 0
    mean = compute_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

# ---------------------------
# TUKEY MEDIAN-OF-HALVES QUARTILES
# ---------------------------
def median_of_list(values: List[float]) -> float:
    values = sorted(values)
    n = len(values)
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    else:
        return (values[mid - 1] + values[mid]) / 2

def percentile_interp(values: List[float], p: float) -> float:
    values = sorted(values)
    n = len(values)
    if n == 0:
        return 0

    # Position using Excel/Google Sheets method
    pos = (n - 1) * (p / 100)
    lower = math.floor(pos)
    upper = math.ceil(pos)

    if lower == upper:
        return values[lower]

    return values[lower] + (values[upper] - values[lower]) * (pos - lower)

def find_outliers(values: List[float]):
    if not values:
        return [], (0, 0)

    q1 = percentile_interp(values, 25)
    q3 = percentile_interp(values, 75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = [v for v in values if v < lower or v > upper]
    return outliers, (round(lower, 2), round(upper, 2))

# ---------------------------
# GROUP STUDENTS BY SECTION
# ---------------------------
def group_by_section(students: List[dict]) -> Dict[str, List[float]]:
    sections = {}
    for s in students:
        sections.setdefault(s["section"], []).append(s["final_grade"])
    return sections

# ---------------------------
# ANALYZE (called from main)
# ---------------------------
def analyze(students: List[dict]) -> None:
    grouped = group_by_section(students)

    print("\n=== ANALYSIS REPORT (Using Median-of-Halves IQR Method) ===")
    for section, scores in grouped.items():
        outliers, bounds = find_outliers(scores)
        
        print(f"\nSection {section}:")
        print("Scores:", scores)
        print(f"Mean: {compute_mean(scores):.2f}")
        print(f"Median: {compute_median(scores):.2f}")
        print(f"Std Dev: {compute_stddev(scores):.2f}")
        print(f"Bounds (Normal Range): {bounds}")

        if outliers:
            formatted = ", ".join(str(round(o, 2)) for o in outliers)
            print(f"Outliers: {formatted}")
        else:
            print("Outliers: None")
