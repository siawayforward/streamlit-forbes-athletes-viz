import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.title('Forbes Richest Athletes 1990-2019')

# streamlit run forbes_list.py for app to load

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

@st.cache
#change data based on EDA changes and cleaning
def load_data(rows):
    data = pd.read_csv('Forbes Richest Athletes 1990-2019.csv')
    data['sports_cat'] = data['Sport'].apply(lambda x: categorize_sports(x))
    del data['Sport'], data['Previous Year Rank'], data['S.NO'] #not interested in index or prev yr
    data.rename(columns={'earnings ($ million)':'Earnings(mil)', 'sports_cat':'Sport'}, inplace=True)
    return data

#Load data with prompts
load_state = st.text('Loading data...')
data = load_data(300)
load_state.text('Loading data... Done!')

#data source and disclaimer
disclaimer = """
    Source: [Kaggle User Dataset](https://www.kaggle.com/parulpandey/forbes-highest-paid-athletes-19902019/data)  
    *Missing data in 2001
    """
#inspecting raw data
if st.button('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)
    st.write(disclaimer)

#Diagrams to display if prompted
#bubble plot by most frequent sport over the years
fig_bubble = px.scatter(data, x='Year', y='Earnings(mil)', log_y=True,
    size='Earnings(mil)',color='Sport',hover_name='Name',
    title='Earnings by Sport 1990-2019')

#USA athletes only
fig_bubble_US = px.scatter(data[data['Nationality']=='USA'], x='Year', y='Earnings(mil)', log_y=True,
    size='Earnings(mil)',color='Sport',hover_name='Name',
    title='Earnings by Sport in the U.S. 1990-2019')

#bar chart for earnings by year
data_four = data[(data['Sport']=='Basketball') | (data['Sport']=='Baseball') |
                (data['Sport']=='NFL') | (data['Sport']=='Hockey')]
fig_bar = px.bar(data_four, x='Year', y='Earnings(mil)', color='Sport', hover_name='Name',
                title='Earnings by Sport 1990-2019')

#heatmap of earnings by sport
fig_map = go.Figure(data=go.Heatmap(
                   z=data['Earnings(mil)'],
                   x=data['Sport'],
                   y=data['Year'],
                   hoverongaps = False))

#Top total earnings by sport distributions
#read text for each figure
graph_options = st.sidebar.selectbox('What would you like to see?',
            ('Select Figure', 'Earnings over Time', 'Top Four Sports: USA', 'Who\'s Winning?'))
#displays
if graph_options == 'Earnings over Time':
    st.write('How sports have become more or less lucrative with list appearances over time')
    st.write(fig_bubble)
    st.write(disclaimer, '\n*Hover over each bubble to see individual athlete details*')
    st.write("""
        **Carrying the Load**

        There is a huge disparity in pay between boxing and other sports; even consistent list visitors
        from basketball. This is mainly driven by *Floyd Mayweather*, who by himself consistently makes
        10 figures for a single fight among other business ventures. Another sport driven by a single
        athlete's earnings in tournament play and endorsements is golf with *Tiger Woods*, who is 
        regarded as the top player of his generation with a career prime that lasted most of the 2000's.
        Even while not playing at the top of the sport for most of the 2010's, he still managed to appear
        on the Forbes list because of how many endorsements he drives. In 2014, Dick's Sporting Goods [let
        go of 500 PGA professionals](https://www.golfchannel.com/article/equipment-insider/report-dicks-fires-more-500-pga-pros),
        a move attributable to Tiger Woods' decline as a prominent figure in golf.

        **Always There When you Call**

        Basketball players have not missed a year on this Forbes top earners list in the last three decades\*.
        In the 1990's Michael Jordan was a constant on the list with earnings from playing and endorsements. 
        This torch was then taken over by the late, great, Kobe Bean Bryant during his storied tenure with the
        Los Angeles 

    """)
if graph_options == 'Top Four Sports: USA':
    st.write('How Basketball, Baseball, Football, and Hockey pay off for their athletes')
    st.write(fig_bar)
    st.write(disclaimer, '\n*Hover over each bar to see individual athlete details*')
    st.write("""
        Over the last 30 years, basketball players have remained the highest earners as individuals.
        Most of them have additional income outside of the NBA that includes branding and shoe deals.
        Football and baseball players are historically less prominent when it comes to sporting goods
        brand endorsement. The same can be said about hockey.

        **For the Love of Hockey**

        An interesting observation is that hockey appears to be an outlier on this list. Forbes features
        it once in 1997. Although the American media classifies this sport as one of the top, revenue and
        compensation, great indicators of interest and influence, declare the opposite. Over the last few 
        decades, compensation is negligible among top contenders, if anything.

        **Will the NFL Catch up?**

        A short answer? No.  
        Football has been the only sport trying to appear consistently on the list, 
        especially in the 2010's. This is mostly because the quarterback market exploded. All footballers
        appearing except for Terrell Suggs are quarterbacks. They are the most valued (in terms of dollars)
        player on the team, and are more likely to end up with national endorsement deals. Even with these 
        strides, it would be hard to pay NFL players like NBA players:
        - There are 53 of them on each team, compared to 15 NBA players. The distribution of income and revenue
        is easier to tie to direct player impacts for NBA superstarts compared to the NFL. You only play on one
        side of the field in football, so your impact can only be represented by so much.
        - The NBA players association has more leverage than their NFL counterparts because of how one player
        can influence a season for the whole league e.g. LeBron James leaving Cleveland the first time and 
        the Eastern Conference in 2010 and 2018 respectively.
    """)
