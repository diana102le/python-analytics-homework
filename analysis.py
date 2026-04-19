import pandas as pd
data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 950, 500]}
df = pd.DataFrame(data)
print("Продажi по містах (тимчасова версія):")
print(df)
print("Середнє значення:", df["sales"].mean())
