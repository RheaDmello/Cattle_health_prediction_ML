import pandas as pd

data = pd.read_csv("milknew.csv")

df = pd.DataFrame(data)

change = {'high': 3, 'medium': 2, 'low': 1}

df['New Grade'] = df['Grade'].map(change)

print(df)
milkData=df.drop(['Grade'], axis=1)

milkData.to_csv('MilkQuality.csv', index=False)

print("Successfull!!!")





