import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date')
df = pd.read_csv("fcc-forum-pageviews.csv")
# print(df.dtypes)
# print(df.shape)
# https://datatofish.com/strings-to-datetime-pandas/
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) 
        & (df['value'] <= df['value'].quantile(0.975))]
# df = pd.DataFrame(df) # similar result without this line 
# print(df.head())
# print(df.dtypes)
# print(df.shape)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 10))  # 

    sns.lineplot(data=df, ax=ax, x='date', y='value', color='red')
    ax.set(xlabel='Date', ylabel='Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
   
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().set_index('date')

    df_bar["month"] = df_bar.index.month
    df_bar["year"] = df_bar.index.year
    df_bar = df_bar.groupby(["year", "month"])["value"].mean()
    # https://betterprogramming.pub/the-best-way-to-group-data-in-pandas-7f446a1fc7fa
    df_bar = df_bar.unstack()

    # print(df_bar)
    # print(df_bar.head())
    # https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.year.html#pandas.DatetimeIndex.year

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(16, 12))

    fig = df_bar.plot(kind ="bar", legend=True, figsize=(12, 8)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    plt.legend(loc='upper left', title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']) 
    # fig = fig.fig

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

# https://seaborn.pydata.org/tutorial/data_structure.html
# https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=box%20plot#seaborn.boxplot

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    sns.boxplot(data=df_box, ax=ax1, x='year', y='value') 
    ax1.set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')

    sns.boxplot(data=df_box, ax=ax2, x='month', y='value', order=['Jan', 'Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
