from fastapi import FastAPI
from wordcloud import WordCloud, STOPWORDS
from ftplib import FTP
import os
import pandas as pd

app = FastAPI()

@app.get("/items/")
async def root_path(country: int = 0, fromdate: int = 10, todate: int = 10):
    if(country==1):
        df = pd.read_csv('Uganda_Hate.csv')
    text = "Guille Guille Guille Luci Luci Luci"
    text = df.clean_text[0]
    wordcloud = WordCloud(stopwords = STOPWORDS,
                                  collocations=True,min_word_length=4,collocation_threshold=3,max_words=2).generate(text)
    text_dict={k: v for k, v in sorted(wordcloud.process_text(text).items(),reverse=True, key=lambda item: item[1])}
    return {"message": text_dict}