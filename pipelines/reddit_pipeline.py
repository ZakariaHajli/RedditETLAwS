import pandas as pd

from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, transform_data, load_data_to_csv
from etls.reddit_etl import extract_posts
def reddit_pipeline( file_name: str , subreddit: str , time_filter='day' , limit=None):
    #connecting to reddit instance
    instance = connect_reddit(CLIENT_ID , SECRET , 'ZakariaEtl')
    #extraction
    posts = extract_posts(instance , subreddit , time_filter , limit)
    post_df = pd.DataFrame(posts)
    #transformation
    post_df = transform_data(post_df)
    #loading to csv
    load_data_to_csv(post_df , f'{OUTPUT_PATH}/{file_name}.csv')



