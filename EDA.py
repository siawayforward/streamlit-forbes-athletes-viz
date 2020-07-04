import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#https://www.kaggle.com/parulpandey/forbes-highest-paid-athletes-19902019/data
df = pd.read_csv('Forbes Richest Atheletes (Forbes Richest Athletes 1990-2019).csv')
data = df.copy()
data.shape #(291 obs, 10 features)

#initial figures for interest
fig, axes = plt.subplots(ncols=2, figsize=(20,8))
axes[0].plot(data.Year, data['earnings ($ million)'])
axes[1].scatter(data.Year, data['earnings ($ million)'])
plt.show()

#sports categorization for earnings
chart = sns.catplot(x='Year', y = 'earnings ($ million)', hue='Sport', data=data)
plt.xticks(rotation=45, horizontalalignment='right')

#clean column //some sports are duplicates because of different case writing
data['sport'] = data['Sport'].apply(lambda x: x.lower().strip())

#redo plot to see categories by sport again
chart = sns.catplot(x='Year', y = 'earnings ($ million)', hue='sport', data=data)
plt.xticks(rotation=45, horizontalalignment='right')

# we still have duplicates. Try to see more general sport category 
# e.g. American Football for NFL or football OR Basketball for NBA, basketball entries
def categorize_sports(sport):
    if sport == 'nfl' or sport == 'american football': return 'NFL'
    if sport == 'nba' or sport == 'basketball': return 'Basketball'
    if 'racing' in sport or 'motor' in sport or 'nascar' in sport: return 'Motorsports'
    if len(sport) <= 3: return sport.upper() #sport abbreviations for leagues
    return sport.title()

#condense even more for sport in general unless league is unique to that sport e.g. NFL
data['sports_cat'] = data['sport'].apply(lambda x: categorize_sports(x))

#redo plot to see sports categories instead of sports names
chart = sns.catplot(x='Year', y = 'earnings ($ million)', hue='sports_cat', data=data)
plt.xticks(rotation=45, horizontalalignment='right')

#category plot with axes switched
plt.figure(figsize=(10,5))
chart = sns.catplot(x='sports_cat', y = 'earnings ($ million)', data=data)
plt.xticks(rotation=45, horizontalalignment='right')

#Sports categories - which sports are most likely to have the highest earners?
plt.figure(figsize=(10,5))
chart = data['sports_cat'].value_counts().plot(kind='bar')
chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right')

#Only the top earner for each year by sport
data_top = data[data['Current Rank'] == 1]
plt.figure(figsize=(10,5))
chart = sns.catplot(x='sports_cat', y= 'earnings ($ million)', data=data_top)
plt.xticks(rotation=45, horizontalalignment='right')

#save to new file for visualization
#interested in slices of athletes, sport, and networth/earnings so will visualize these mostly
#will delete previous year ranking, generalize sports categories because most athletes play one sport

