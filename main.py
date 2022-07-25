from fastapi import FastAPI
from wordcloud import WordCloud, STOPWORDS
from ftplib import FTP
import os
import pandas as pd
import re

app = FastAPI()

@app.get("/items/")
async def root_path(country: int = 1, fromdate: str = '2022-01-01T00:00:00', todate: str = '2022-01-31T00:00:00', topic: int = 0):
    if(country==1):
        str_topic = "Uganda_"+str(topic)+".csv"
    elif(country==2):
        str_topic = "Colombia_"+str(topic)+".csv"
    elif(country==3):
        str_topic = "Philippines_"+str(topic)+".csv"
    df = pd.read_csv(str_topic)
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:%S')
    filtered_df = df.loc[(df['date'] >= fromdate)
                     & (df['date'] < todate)]
    out = filtered_df['clean_text']
    text = "".join(str(out))

    new_string = re.sub(r'[0-9]', '', text)
    new_string = re.sub(r'\n', '', new_string)
    new_string = re.sub(r'Name: clean_text, Length: , dtype: object', '', new_string)

    wordcloud = WordCloud(stopwords = STOPWORDS,
                                  collocations=True,min_word_length=4,collocation_threshold=3,max_words=1).generate(new_string)
    text_dict={k: v for k, v in sorted(wordcloud.process_text(new_string).items(),reverse=True, key=lambda item: item[1])}
    return {"message": text_dict}