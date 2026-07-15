import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df = df.drop(columns=["Cabin"])
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

survival_by_class = df.groupby("Pclass")["Survived"].mean()
print(survival_by_class)

survival_by_class.plot(kind="bar", color=["gold", "silver", "brown"])
plt.title("Titanic Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.savefig("survival_by_class.png", dpi=100, bbox_inches="tight")
print("Chart saved!")
