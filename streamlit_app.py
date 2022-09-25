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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response.json())

# normalize the json file
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
