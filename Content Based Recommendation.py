# ### Creating TF-IDF Matris

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1500)
pd.set_option('display.expand_frame_repr', False)
# https://www.kaggle.com/rounakbanik/the-movies-dataset
df = pd.read_csv(".datasets/movies_metadata.csv", low_memory=False)  # to ignore "DtypeWarning" I did "low_memory=False"


# stop_words means: to ignore the words that there are no meaning by themselves (and, the, on...)
tfidf = TfidfVectorizer(stop_words="english")
# to avoid "NaN" counting as a word, I need to change "NaN" values, in "overview", with ''.
df['overview'] = df['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df['overview'])


# ### Cosine Similarity Matrix

cosine_sim = cosine_similarity(tfidf_matrix)


# ### Recommendations according to the similarity

indices = pd.Series(df.index, index=df['title'])
indices = indices[~indices.index.duplicated(keep='last')]
movie_index = indices["Sherlock Holmes"]
similarity_scores = pd.DataFrame(cosine_sim[movie_index],columns=["score"])
movie_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index
recommendations = df['title'].iloc[movie_indices]

# ### Function:


def content_based_recommender(title, cosine_sim, dataframe):

    indices = pd.Series(dataframe.index, index=dataframe['title'])
    indices = indices[~indices.index.duplicated(keep='last')]

    movie_index = indices[title]

    similarity_scores = pd.DataFrame(cosine_sim[movie_index], columns=["score"])

    movie_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index
    return dataframe['title'].iloc[movie_indices]


content_based_recommender("The Matrix", cosine_sim, df)
content_based_recommender("The Hobbit", cosine_sim, df)
content_based_recommender("The Godfather", cosine_sim, df)

