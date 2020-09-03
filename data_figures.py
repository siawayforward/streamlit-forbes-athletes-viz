#modules
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# we have duplicates. Trying to see more general sport category 
# e.g. American Football for NFL or football OR Basketball for NBA, basketball entries
def categorize_sports(sport):
    sport = sport.lower()
    if sport == 'nfl' or sport == 'american football': return 'NFL'
    if sport == 'nba' or sport == 'basketball': return 'Basketball'
    if '/' in sport: return 'Two-Sport Athlete'
    if 'racing' in sport or 'motor' in sport or 'nascar' in sport: return 'Motorsports'
    if len(sport) <= 3: return sport.upper() #sport abbreviations for leagues
    return sport.title()

#change data based on EDA changes and cleaning
def load_data(rows):
    data = pd.read_csv('Forbes Richest Athletes 1990-2019.csv')
    data['sports_cat'] = data['Sport'].apply(lambda x: categorize_sports(x))
    del data['Sport'], data['Previous Year Rank'], data['S.NO'] #not interested in index or prev yr
    data.rename(columns={'earnings ($ million)':'Earnings(mil)', 'sports_cat':'Sport'}, inplace=True)
    return data

#Diagrams to display if prompted
def get_earnings_over_time(data):
    #bubble plot by most frequent sport over the years
    fig_bubble = px.scatter(data, x='Year', y='Earnings(mil)', log_y=True,
        size='Earnings(mil)',color='Sport',hover_name='Name',
        title='Earnings by Sport 1990-2019')

    #USA athletes only
    fig_bubble_US = px.scatter(data[data['Nationality']=='USA'], x='Year', y='Earnings(mil)', log_y=True,
        size='Earnings(mil)',color='Sport',hover_name='Name',
        title='Earnings by Sport in the U.S. 1990-2019')

    return [fig_bubble, fig_bubble_US]

def get_US_sports(data):
    #bar chart for earnings by year
    data_four = data[(data['Sport']=='Basketball') | (data['Sport']=='Baseball') |
                    (data['Sport']=='NFL') | (data['Sport']=='Hockey')]
    fig_bar = px.bar(data_four, x='Year', y='Earnings(mil)', color='Sport', hover_name='Name',
                    title='Earnings by Sport 1990-2019')
    return fig_bar

def get_highest_earners(data):
    #earnings by athlete (who earns the highest?) top 10 earners
    earnings = pd.DataFrame(data[['Name', 'Earnings(mil)']])
    earnings = earnings.groupby(by=['Name']).sum().sort_values(by=['Earnings(mil)'], 
                                ascending=False)
    earnings_top10 = earnings[:10]
    fig, axes = plt.subplots(ncols=2, figsize=(15, 6))
    sns.barplot(x=data['Name'].value_counts().index[:10], y=data['Name'].value_counts().values[:10], ax=axes[0])
    sns.barplot(x=earnings_top10['Name'], y=earnings_top10['Earnings(mil)'], ax=axes[1])
    axes[0].set_title('Most Forbes List Appearances: 1990-2019')
    axes[1].set_title('Highest Earners acc. to Forbes: 1990-2019')
    return fig
