#import package
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time
import Directory
import os
from functions import *
import string
import random
from pathlib import Path
from PIL import Image
import webbrowser

st.title('Wordcloud and LDA on review sites')

# Set up Side Bar
st.sidebar.title('Please enter the model information')

st.sidebar.markdown('Example URL: url1 + increment_string + increment + url2')

url1 = st.sidebar.text_input('url1: The first part of the url string that remains constant between review pages', 'https://www.tripadvisor.co.uk/Attraction_Review-g190384-d6755801-Reviews')
url2 = st.sidebar.text_input('url2: The second part of the url string that remains constant between review pages', '-The_House_of_Dionysus-Paphos_Paphos_District.html')
increment_string1 = st.sidebar.text_input('increment_string: The part of the url string which precedes the page change', '-or')
increment_string2 = ''
#st.sidebar.text_input('increment_string2: The part of the url string which comes after the page change', '')
total_pages = st.sidebar.number_input('total_pages', 2)
increment = st.sidebar.number_input('increment: The part of the string which comes after the page change',min_value = 0,value = 5)
#site = st.sidebar.text_input('site', 'tripadvisor')
site = st.sidebar.selectbox('Site', ['tripadvisor','yelp'])
filename = ''

topic_num = st.sidebar.number_input('Number Of Topics',min_value = 2,value = 2)

for i in range(4):
    filename = filename + random.choice(string.ascii_letters)

if st.button('Run Model'):
    ms = WebScraper.WebScraper(site=site,url1=url1,
                          url2=url2,increment_string1=increment_string1,increment_string2=increment_string2,
                          total_pages=int(total_pages),increment=int(increment),silent=False)

    ms.fullscraper()

    filePath = Directory.outputPath
    #if filename=='':
    #    for i in range(4):
    #        filename = filename + random.choice(string.ascii_letters)

    filename = 'output'

    myTopicModel = TopicModeling.TopicModeling(ms.all_reviews)

    myTopicModel.ldaFromReviews(topics = topic_num)

    myTopicModel.generate_wordcloud()

    save_path_wc = os.path.join(filePath,'static',filename + '.png')
    save_dir_wc = os.path.join(filePath,'static')
    Path(save_dir_wc).mkdir(parents=True, exist_ok=True)
    myTopicModel.saveWordcloud(save_path_wc)

    image2 = Image.open(save_path_wc)
    st.image(image2, use_column_width=True)

    st.write('Higher coherence scores relate to a better prediction in the number of topics')
    st.write('Topics = {}, Coherence = {}'.format(topic_num,myTopicModel.coherence_lda))
    save_path_LDA = os.path.join(filePath,'templates','LDAhtmls',filename + '.html')
    Path(os.path.sep.join(save_path_LDA.split(os.path.sep)[:-1])).mkdir(parents=True, exist_ok=True)
    myTopicModel.saveLDA(save_path_LDA)
    webbrowser.open_new_tab(save_path_LDA)
    
    st.dataframe(ms.all_reviews)

