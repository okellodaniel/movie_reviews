import io
import os
import pandas as pd
import requests
import zipfile

from kaggle.api.kaggle_api_extended import KaggleApi

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def kaggle_downloader(dataset_path):
    os.environ['KAGGLE_USERNAME'] = 'danielokello'
    os.environ['KAGGLE_KEY'] = 'bccfbb5a23280265af48816d6a03bd35'

    api = KaggleApi()
    api.authenticate()

    return api.dataset_download_files(dataset_path, path="./dataset")


def unzip_dataset(zip_filepath,dest_dir):
    """
    Unzip a zip file.

    Parameters:
    zip_filepath (str): The path to the zip file.
    dest_dir (str): The directory to extract files to.
    """
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(dest_dir)

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    dataset_name = 'movies-review'
    url = f'jaidalmotra/{dataset_name}'
    kaggle_downloader(url)

    unzip_dataset(f'./dataset/{dataset_name}.zip', './dataset')

    data_dict = {
    "name": str,
    "year": int,
    "movie_rated": str,
    "run_length": str,
    "genres": str,
    "release_date": str,
    "rating": float,
    "num_raters": int,
    "num_reviews": int,
    "review_url": str
    }   

    df_action = pd.read_csv('./dataset/1_movies_per_genre/Action.csv',sep=',',dtype=data_dict)
    df_adventure = pd.read_csv('./dataset/1_movies_per_genre/Adventure.csv',sep=',',dtype=data_dict)
    df_animation = pd.read_csv('./dataset/1_movies_per_genre/Animation.csv',sep=',',dtype=data_dict)
    df_biography = pd.read_csv('./dataset/1_movies_per_genre/Biography.csv',sep=',',dtype=data_dict)
    df_comedy = pd.read_csv('./dataset/1_movies_per_genre/Comedy.csv',sep=',',dtype=data_dict)
    df_crime = pd.read_csv('./dataset/1_movies_per_genre/Crime.csv',sep=',',dtype=data_dict)
    df_drama = pd.read_csv('./dataset/1_movies_per_genre/Drama.csv',sep=',',dtype=data_dict)
    df_fantasy = pd.read_csv('./dataset/1_movies_per_genre/Fantasy.csv',sep=',',dtype=data_dict)
    df_history = pd.read_csv('./dataset/1_movies_per_genre/History.csv',sep=',',dtype=data_dict)
    df_horror = pd.read_csv('./dataset/1_movies_per_genre/Horror.csv',sep=',',dtype=data_dict)
    df_music = pd.read_csv('./dataset/1_movies_per_genre/Music.csv',sep=',',dtype=data_dict)
    df_mystery = pd.read_csv('./dataset/1_movies_per_genre/Mystery.csv',sep=',',dtype=data_dict)
    df_romance = pd.read_csv('./dataset/1_movies_per_genre/Romance.csv',sep=',',dtype=data_dict)
    df_scifi = pd.read_csv('./dataset/1_movies_per_genre/Sci-Fi.csv',sep=',',dtype=data_dict)
    df_sport = pd.read_csv('./dataset/1_movies_per_genre/Sport.csv',sep=',',dtype=data_dict)
    df_thriller = pd.read_csv('./dataset/1_movies_per_genre/Thriller.csv',sep=',',dtype=data_dict)
    df_war = pd.read_csv('./dataset/1_movies_per_genre/War.csv',sep=',',dtype=data_dict)


    
    return pd.concat([df_action,df_adventure,df_animation,df_biography,df_comedy,df_crime,df_drama,df_fantasy,df_history,df_horror,df_music,df_mystery,df_scifi,df_sport,df_thriller,df_romance,df_war],ignore_index=True)

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
