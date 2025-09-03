import streamlit as st
import time
import numpy as np
import pandas as pd

st.write("Hello World")


#st.write("df = pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]})df")
#df = pd.DataFrame({
#  'first column': [1, 2, 3, 4],
#  'second column': [10, 20, 30, 40]
#})
#df




#st.write("st.write(pd.Dataframe({'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]}))")
#st.write(pd.DataFrame({
#    'first column': [1, 2, 3, 4],
#    'second column': [10, 20, 30, 40]
#}))




#st.write("chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])st.line_chart(chart_data)")
#chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])
#st.line_chart(chart_data)




#st.write("map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])st.map(map_data)")
#map_data = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#    columns=['lat', 'lon'])
#st.map(map_data)




#st.write("x = st.slider('x')  # 👈 this is a widget \n st.write(x, 'squared is', x * x)")
#x = st.slider('x')  # 👈 this is a widget
#st.write(x, 'squared is', x * x)
#st.write(" ")




#st.write("st.text_input('Your name', key='name') st.session_state.name")
#st.text_input("Your name", key="name")
# You can access the value at any point with:
#st.session_state.name




#st.write("if st.checkbox('Show dataframe'):chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])chart_data")
#if st.checkbox('Show dataframe'):
#    chart_data = pd.DataFrame(
#       np.random.randn(20, 3),
#       columns=['a', 'b', 'c'])
#    chart_data




#st.write("df = pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]})option = st.selectbox('Which number do you like best?', df['first column'])'You selected: ', option")
#df = pd.DataFrame({
#    'first column': [1, 2, 3, 4],
#    'second column': [10, 20, 30, 40]
#    })
#option = st.selectbox(
#    'Which number do you like best?',
#     df['first column'])
#'You selected: ', option




# Add a selectbox to the sidebar:
#add_selectbox = st.sidebar.selectbox(
#    "add_selectbox = st.sidebar.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))  "\
#    "  How would you like to be contacted?",
#    ('Email', 'Home phone', 'Mobile phone')
#)
# Add a slider to the sidebar:
#add_slider = st.sidebar.slider(
#    "add_slider = st.sidebar.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))  " \
#    "  Select a range of values",
#    0.0, 100.0, (25.0, 75.0)
#)
#st.write(" ")
#st.write(" ")



#st.write("left_column, right_column = st.columns(2)left_column.button('Press me!')with right_column:chosen = st.radio('Sorting hat',('Gryffindor', 'Ravenclaw, 'Hufflepuff', 'Slytherin'))st.write(f'You are in {chosen} house!')")
#left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
#left_column.button('Press me!')
# Or even better, call Streamlit functions inside a "with" block:
#with right_column:
#    chosen = st.radio(
#        'Sorting hat',
#        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#    st.write(f"You are in {chosen} house!")




#st.write("")
#'Starting a long computation...'
# Add a placeholder
#latest_iteration = st.empty()
#bar = st.progress(0)

#for i in range(100):
  # Update the progress bar with each iteration.
#  latest_iteration.text(f'Iteration {i+1}')
#  bar.progress(i + 1)
#  time.sleep(0.1)
#'...and now we\'re done!'



#st.write("")
# Define the pages
#main_page = st.Page("app.py", title="Main Page", icon="🎈")
#page_2 = st.Page("page_2.py", title="Page 2", icon="❄️")
#page_3 = st.Page("page_3.py", title="Page 3", icon="🎉")
# Set up navigation
#pg = st.navigation([main_page, page_2, page_3])
# Run the selected page
#pg.run()


####################################################
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
#data_load_state.text('Loading data...done!')

data_load_state.text("Done! (using st.cache_data)")
