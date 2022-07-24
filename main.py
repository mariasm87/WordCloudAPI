from fastapi import FastAPI
from wordcloud import WordCloud, STOPWORDS

app = FastAPI()

text = "esto es una prueba"


@app.get("/items/")
async def read_item(country: int = 0, fromdate: int = 10, todate: int = 10):
    text_dictionary = wordcloud.process_text(text)
    word_freq={k: v for k, v in sorted(text_dictionary.items(),reverse=True, key=lambda item: item[1])}
    return list(word_freq.items())[:5]