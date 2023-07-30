import pandas as pd

df = pd.read_csv('records.txt', delimiter=' ')
print(df.sort_values(by='Time', ascending=False))