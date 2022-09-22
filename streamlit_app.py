import streamlit
streamlit.title('My Parents new healthy dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 kale, spinach & Rocket smoothie')
streamlit.text('🐔 Hard-boiled Free-Range egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
