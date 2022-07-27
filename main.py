from fastapi import FastAPI
from wordcloud import WordCloud, STOPWORDS
from ftplib import FTP
import os
import pandas as pd
import re
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/items/")
async def root_path(country: int = 1, fromdate: str = '2022-01-01T00:00:00', todate: str = '2022-01-31T00:00:00', topic: int = 0):
    if(country==1):
        if(topic==0):
            df1 = pd.read_csv("Uganda_1.csv")
            df2 = pd.read_csv("Uganda_2.csv")
            df3 = pd.read_csv("Uganda_3.csv")
            df4 = pd.read_csv("Uganda_4.csv")
            df5 = pd.read_csv("Uganda_5.csv")
            df = pd.concat([df1,df2,df3,df4,df5])
        else:
            str_topic = "Uganda_"+str(topic)+".csv"
            df = pd.read_csv(str_topic)
    elif(country==2):
        if(topic==0):
            df1 = pd.read_csv("Colombia_1.csv")
            df2 = pd.read_csv("Colombia_2.csv")
            df3 = pd.read_csv("Colombia_3.csv")
            df4 = pd.read_csv("Colombia_4.csv")
            df5 = pd.read_csv("Colombia_5.csv")
            df = pd.concat([df1,df2,df3,df4,df5])
        else:
            str_topic = "Colombia_"+str(topic)+".csv"
            df = pd.read_csv(str_topic)
    elif(country==3):
        if(topic==0):
            df1 = pd.read_csv("Philippines_1.csv")
            df2 = pd.read_csv("Philippines_2.csv")
            df3 = pd.read_csv("Philippines_3.csv")
            df4 = pd.read_csv("Philippines_4.csv")
            df5 = pd.read_csv("Philippines_5.csv")
            df = pd.concat([df1,df2,df3,df4,df5])
        else:
            str_topic = "Philippines_"+str(topic)+".csv"
            df = pd.read_csv(str_topic)
    
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:%S')
    filtered_df = df.loc[(df['date'] >= fromdate)
                     & (df['date'] < todate)]
    out = filtered_df['clean_text']
    text = "".join(str(out))

    new_string = ''.join([i for i in text if not i.isdigit()])
    new_string = new_string.strip()
    new_string = new_string.replace("Name: clean_text, Length: , dtype: object","")

    wordcloud = WordCloud(stopwords = STOPWORDS,
                                  collocations=True,min_word_length=4,collocation_threshold=6,max_words=2).generate(new_string)
    text_dict={k: v for k, v in sorted(wordcloud.process_text(new_string).items(),reverse=True, key=lambda item: item[1])}
    return {"message": text_dict}