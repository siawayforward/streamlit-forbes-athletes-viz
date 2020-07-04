import streamlit as st 
import pandas as pd
import numpy as np

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
    data = pd.read_csv('Forbes Richest Atheletes (Forbes Richest Athletes 1990-2019).csv')
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

#histogram by most frequent sport on list
st.subheader('List Appearances by Sport')
sport_ct = pd.DataFrame(data['Sport'].value_counts())
st.bar_chart(sport_ct)
