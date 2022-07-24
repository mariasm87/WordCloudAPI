from fastapi import FastAPI
from wordcloud import WordCloud, STOPWORDS

app = FastAPI()

@app.get("/items/")
async def root_path(country: int = 0, fromdate: int = 10, todate: int = 10):
    text = "Esto es una prueba prueba y me gusta intentar mejorarla"
    wordcloud = WordCloud(stopwords = STOPWORDS,
                                  collocations=True,min_word_length=4,collocation_threshold=3,max_words=2).generate(text)
    text_dict={k: v for k, v in sorted(wordcloud.process_text(text).items(),reverse=True, key=lambda item: item[1])}
    return {"message": text_dict}