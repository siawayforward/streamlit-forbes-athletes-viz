import streamlit as st 
import data_figures as dfig

# streamlit run forbes_list.py for app to load
st.title('Forbes Richest Athletes 1990-2019')
#data items
#@st.cache
loadstate = st.text('Loading data')
data = None
data = dfig.load_data(300)

#figures
fig_bubbles, fig_bar, fig = [[None, None], None, None]
figs_bubbles = dfig.get_earnings_over_time(data)
fig_bar = dfig.get_US_sports(data)
fig = dfig.get_highest_earners(data)
loadstate.text('Loading data... Done!')

#Load data with prompts

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


#Top total earnings by sport distributions
#read text for each figure
graph_options = st.sidebar.selectbox('What would you like to see?',
            ('Select Figure', 'Earnings over Time', 'Top Four Sports: USA', 'Who\'s Winning?'))
#displays
if graph_options == 'Earnings over Time':
    st.subheader('How sports have become more or less lucrative with list appearances over time')
    #show by US vs World
    US_only = st.checkbox('See US Athletes only')
    if US_only:
        st.write(figs_bubbles[1])
    else:
        st.write(figs_bubbles[0])
    st.write(disclaimer, '\n*Hover over each bubble to see individual athlete details*')
    st.write("""
        **Carrying the Load**

        There is a huge disparity in pay between boxing and other sports in the last decade; even consistent 
        list visitors from basketball. This is mainly driven by *Floyd Mayweather*, who by himself consistently 
        makes 10 figures for a single fight among other business ventures. Another sport driven by a single
        athlete's earnings in tournament play and endorsements is golf with *Tiger Woods*, who is 
        regarded as the top player of his generation with a career prime that lasted most of the 2000's.
        Even while not playing at the top of the sport for most of the 2010's, he still managed to appear
        on the Forbes list because of how many endorsements he drives. In 2014, Dick's Sporting Goods [let
        go of 500 PGA professionals](https://www.golfchannel.com/article/equipment-insider/report-dicks-fires-more-500-pga-pros),
        a move attributable to Tiger Woods' decline as a prominent figure in golf.

        **Always There When you Call**

        Basketball players have not missed a year on this Forbes top earners list in the last three decades\*.
        In the 1990's *Michael Jordan* was a constant on the list with earnings from playing and endorsements. 
        This torch was then taken over by the late, great, *Kobe Bean Bryant* during his storied tenure with the
        Los Angeles and then *LeBron James* in the new millenium. Some other athletes who have appeared from the
        NBA include *Steph Curry* and *Shaquille O'Neal*.

        **USA Athletes**

        Isolating the list to just the United States indicates a bulk of them compose the Forbes list. In this
        viewing, the basketball appearances are more prominently seen as consistent over the last three decades. 
        Boxing earnings would change hands by athletes in the early 1990's and it quieted down until the rise of
        *Floyd Mayweather*. Likewise, golf was mainly dominated by the prime of *Tiger Woods*.

    """)

if graph_options == 'Top Four Sports: USA':
    st.subheader('How Basketball, Baseball, Football, and Hockey pay off for their athletes')
    st.write(fig_bar)
    st.write(disclaimer, '\n*Hover over each bar to see individual athlete details*')
    st.write("""
        Over the last 30 years, basketball players have remained the highest earners as individuals.
        Most of them have additional income outside of the NBA that includes branding and shoe deals.
        Football and baseball players are historically less prominent when it comes to sporting goods
        brand endorsement. The same can be said about hockey. It would be interesting to explore a data
        set that shows the split between game income and endorsement income to compare between sports.

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
        can influence a season for the whole league e.g. *LeBron James* leaving Cleveland the first time and 
        the Eastern Conference in 2010 and 2018 respectively.

        **Big Winners don't Earn Big**  
        Except for basketball and individual sports like golf and boxing, the players who have the highest 
        paying contracts do not necessarily have the most championships. *Alex Rodriguez* won once with two of
        baseball's most expensive contracts, and quarterbacks like *Matt Stafford*, *Aaron Rodgers* (hello NFC
        North!), and *Andrew Luck* have made the Forbes list without having a championship in the years before
        and after their list appearances.
    """)

if graph_options == 'Who\'s Winning?':
    st.subheader('Who has the most earnings and list appearances between 1990-2019')
    st.write(fig)
    st.write(disclaimer, '\n*Click zoom arrows to see distribution more clearly*')
    st.write("""
        *Tiger Woods*, though appearing on the list x less times than 19 time leading *Michael Jordan* has the 
        most earnings over the 30 year span. Of note is that this income also includes his endorsement deals with
        various companies, even after losing a lot of them in 2008. Individual sport athletes have been able to 
        accumulate a large amount of wealth in shorter periods of time compared to team sport athletes. Even 
        Michael Jordan, who still appears on the list years after retiring, makes most of his income on merchandise 
        from the Jordan Brand at Nike. LeBron James, who is part of the transition to the new wave of athletes, 
        is climbing up the list, having ventured into the entertainment industry and collaborating with his childhood 
        friend on athlete management. Again, though not atop the list, basketball seems like the best sport to be a 
        part of for consistent higher levels of income *for superstar players*.  
    """)