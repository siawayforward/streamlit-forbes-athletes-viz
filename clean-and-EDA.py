import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#https://www.kaggle.com/parulpandey/forbes-highest-paid-athletes-19902019/data
df = pd.read_csv('Forbes Richest Atheletes (Forbes Richest Athletes 1990-2019).csv')
data = df.copy()

#initial figures for interest
fig, ax = plt.subplots()
plt.plot(data.Year, data['earnings ($ million)'])
plt.show()

#sports categorization for earnings
sns.catplot(x='Year', y = 'earnings ($ million)', hue='Sport', data=data)
plt.show()

#clean column //some sports are duplicates because of different case writing
data['sport'] = data['Sport'].apply(lambda x: x.lower().strip())

#redo plot to see categories by sport again
sns.catplot(x='Year', y = 'earnings ($ million)', hue='sport', data=data)
plt.show()

# we still have duplicates. Try to see more general sport category 
# e.g. American Football for NFL or football OR Basketball for NBA, basketball entries
def categorize_sports(sport):
    if sport == 'nfl' or sport == 'american football': return 'NFL'
    if sport == 'nba' or sport == 'basketball': return 'Basketball'
    if 'racing' in sport or 'motor' in sport or 'nascar' in sport: return 'Motorsports'
    if len(sport) <= 3: return sport.upper() #sport abbreviations for leagues
    return sport.title()

data['sports_cat'] = data['sport'].apply(lambda x: categorize_sports(x))

#redo plot to see sports categories instead of sports names
sns.catplot(x='Year', y = 'earnings ($ million)', hue='sports_cat', data=data)
plt.show()



