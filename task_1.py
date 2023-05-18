import pandas as pd

if __name__ == '__main__':
    ratings_data = pd.read_csv('csv/ratings.csv')
    movies_data = pd.read_csv('csv/movies.csv')

    five_star_ratings = ratings_data[ratings_data['rating'] == 5.0]

    most_rated_movie = five_star_ratings['movieId'].value_counts().idxmax()
    most_rated_movie_details = movies_data[movies_data['movieId'] == most_rated_movie]

    print(most_rated_movie_details[['title', 'genres']])
