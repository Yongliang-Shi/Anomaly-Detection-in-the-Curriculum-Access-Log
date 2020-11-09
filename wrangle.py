import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

# %%
def wrangle_curriculum_access_log():
    # Load the curriculum access dataset
    df_log = pd.read_csv('anonymized-curriculum-access.txt',
                        engine='python',
                        header=None,
                        index_col=False,
                        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
                        na_values='"-"')
    # Load the cohort info dataset
    df_cohort = pd.read_csv('cohorts.csv')
    
    # Rename the columns of df_log
    df_log.columns = ['date', 'time', 'page_accessed', 'user_id', 'cohort_id', 'ip']
    
    # Merge the two datasets
    df = df_log.merge(df_cohort, how='left', on='cohort_id')
    
    # Create a new column for timestamp
    df['timestamp'] = df.date.str.cat(df.time, sep=' ')

    # Conver to datetime dtype
    df.timestamp = pd.to_datetime(df.timestamp)

    # Set the timestamp as index
    df = df.set_index('timestamp').sort_index()

    # Drop columns: date and time
    df.drop(columns=['date', 'time'], inplace=True)

    # Convert the start and end dates to datetime dtpye
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)

    # Create a table to show lessons
    df_pages = df.page_accessed
    df_pages.replace('/', 'homepage', inplace=True)
    df_pages = df_pages.str.split('/', n=1, expand=True)
    df_pages.columns = ['lesson', 'sublesson']

    # Concat the lesson columns to the original dataframe
    df = pd.concat([df, df_pages], axis=1)

    # Drop the column page_accessed
    df.drop(columns='page_accessed', inplace=True)
    return df