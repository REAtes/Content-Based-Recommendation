# Content-Based Movie Recommender System

## Business Problem

The goal of this project is to build a content-based movie recommender system. The system provides movie recommendations to users based on the content and descriptions of movies they have shown interest in.

## Dataset

The dataset used for this project is the [Movies Metadata](https://www.kaggle.com/rounakbanik/the-movies-dataset) dataset, which includes information about movies such as titles, overviews, and more. This dataset is used to create a content-based recommendation system.

## Task

### Creating TF-IDF Matrix
1. Load the movie dataset containing movie metadata.
2. Utilize the TF-IDF (Term Frequency-Inverse Document Frequency) vectorization technique to transform the movie overviews into numerical feature vectors.
3. Calculate the cosine similarity between movies based on their overviews, resulting in a cosine similarity matrix.

### Recommendations according to Similarity
1. Provide recommendations for a specific movie based on the similarity of its content to other movies in the dataset.
2. Recommend the top 10 movies that are most similar to the chosen movie.
3. Implement the `content_based_recommender` function to generate recommendations for different movies.

## Usage

Users can input the title of a movie they are interested in, and the recommender system will return a list of movies that are most similar to the input movie. This can help users discover new movies with content similar to the ones they already like.

## Results

The content-based movie recommender system offers movie recommendations based on textual content and descriptions. By analyzing the content similarities between movies, this system helps users find other movies that align with their preferences and interests. It can be a valuable tool for movie enthusiasts looking to discover new films they may enjoy.

Feel free to explore and customize this system by trying out different movie titles or adapting it to your specific use case.

