import pandas as pd

# l = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
# df = pd.DataFrame(l, columns=["a", "b", "c"])
# print(df)
# print(df.groupby(by=["b"]).sum())
# print(df.groupby(by=["b"], dropna=False).sum())  # TypeError: groupby() got an unexpected keyword argument 'dropna'

df = pd.read_csv("fcc-forum-pageviews.csv")
# print(df.dtypes)
# print(df.shape)
# https://datatofish.com/strings-to-datetime-pandas/

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) 
        & (df['value'] <= df['value'].quantile(0.975))]


df_bar = df.copy()
df_bar['month'] = [d.strftime('%b') for d in df_bar.date]
df_bar['year'] = [d.year for d in df_bar.date]
print(df_bar)