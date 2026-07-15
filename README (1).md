# Titanic Survival Analysis — Project 1

My first data analysis project, built while learning Python for Data Science.

## What it does

- Loads the Titanic passenger dataset (891 passengers)
- Cleans missing data:
  - `Age` — filled missing values with the column mean
  - `Cabin` — dropped entirely (687 of 891 values were missing — too sparse to reliably fill)
  - `Embarked` — filled the 2 missing values with the most common port (mode)
- Answers the question: **"Did passenger class affect survival rate?"**
- Visualizes the result as a bar chart

## Result

| Passenger Class | Survival Rate |
|---|---|
| 1st Class | 62.9% |
| 2nd Class | 47.3% |
| 3rd Class | 24.2% |

First-class passengers were roughly 2.5x more likely to survive than third-class passengers.

## How to run

```bash
pip install pandas matplotlib
python titanic_analysis.py
```

## Tools used

Python, Pandas, Matplotlib
