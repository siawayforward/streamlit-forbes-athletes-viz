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

#inspecting raw data
st.subheader('Raw Data')
st.write(data)

#bubble plot by most frequent sport over the years
fig_bubble = px.scatter(data, x='Year', y='Earnings(mil)', log_y=True,
    size='Earnings(mil)',color='Sport',hover_name='Name',
    title='Earnings by Sport 1990-2019')

#heatmap of earnings by sport
fig_map = go.Figure(data=go.Heatmap(
                   z=data['Earnings(mil)'],
                   x=data['Sport'],
                   y=data['Year'],
                   hoverongaps = False))

#Top five total earnings by sport distributions
#displays
if st.button('See Earnings over Time'):
    st.write('The figure below shows how top earnings evolve over three decades with sport '+
    'differentiations shown. Hover over each bubble to see individual athlete earnings')
    st.write(fig_bubble)
if st.button('See Earnings by Sport'):
    st.write('The heatmap shows which sports have become more or less lucrative with list ' +
    'appearances and dollars over time')
    st.write(fig_map)
