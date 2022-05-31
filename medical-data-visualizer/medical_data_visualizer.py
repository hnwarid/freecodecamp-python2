import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
# print(df.shape)

# Add 'overweight' column
df['overweight'] = (df['weight'] / (df['height'] / 100)**2).apply(lambda x: 1 if x > 25 else 0)
# print(df['overweight'].head())

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
# print(df['cholesterol'].value_counts())
# print(df['gluc'].value_counts())

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
# print(df['cholesterol'].value_counts())
# print(df['gluc'].value_counts())


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'],  value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # print(df_cat.head())
    # print(df_cat.tail())
  
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You wilntl have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])
    # print(df_cat.head())
    df_cat = pd.DataFrame(df_cat['value'].count())
    df_cat = df_cat.rename(columns={'value':'total'}) 
    df_cat = df_cat.reset_index() #     ValueError: cannot insert value, already exists
    # print(df_cat) 

    # Draw the catplot with 'sns.catplot()' 
# https://seaborn.pydata.org/generated/seaborn.catplot.html
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')

    fig = fig.fig #into matplotlib object to pass the 2 test cases

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

  
# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df['overweight'] = (df['weight'] / (df['height'] / 100)**2)
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
                & (df['height'] >= df['height'].quantile(0.025)) 
                & (df['height'] <= df['height'].quantile(0.975))
                & (df['weight'] >= df['weight'].quantile(0.025))
                & (df['weight']) <= df['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle]
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,8))  #figsize syntax error :| 

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, cbar=True, mask=mask, square=True, fmt='.1f', vmax=.3, cbar_kws={'shrink':0.5}, center=0, linewidths=1).figure

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
