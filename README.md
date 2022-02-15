# streamlit-forbes-athletes

Data cleaning and streamlit mini-project to visualize top athlete earners from 1990-2019 with different slices. The objective of this display is to practice using data visualization modules and packages in Python and web-hosting with the streamlit library.

To view this project online, [go here and follow the prompts](https://forbes-top-athlete-earners.herokuapp.com/)

To run this on your local system, follow the instructions below:

## Pre-requisites

- Install streamlit library `pip install streamlit`, along with `matplotlib`, `seaborn`, and `plotly`
- Download the data and script files `Forbes Richest Athletes 1990-2019.csv` and `forbes_list.py`
- If you'd like to access the original dataset online, it can be found [here](https://www.kaggle.com/parulpandey/forbes-highest-paid-athletes-19902019/data)
- In your terminal enter the following command

```cmd
streamlit run forbes_list.py
```

This will open a localhost browser and allow you to see the data and accompanying visualizations. There is a filter option for some of the graphics to drill down to the sport or country and drill up to the total number of athletes in the list from a specific sport.

**Note:** You can also go directly to the app where this is hosted on [Streamlit Cloud](https://share.streamlit.io/siawayforward/streamlit-forbes-athletes-viz/forbes_list.py)
