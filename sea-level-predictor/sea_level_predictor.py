import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.subplots(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], marker='.', color='yellow').figure
    # https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.scatter.html

    # Create first line of best fit
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
    # https://towardsdatascience.com/simple-and-multiple-linear-regression-with-python-c9ab422ec29c
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    plt.plot(x1, res1.slope*x1+res1.intercept, label='first line of best fit', color='orange', linewidth=0.5)

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    # print(df2)
    res2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    plt.plot(x2, res2.slope*x2+res2.intercept, label='second line of best fit', color='red', linewidth=0.5)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
