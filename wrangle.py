import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

# %%
def wrangle_curriculum_access_log():
    """
    The function is used to acquire and prepare the curriculum access log dataset.
    """
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
    
    # Replace / with homepage
    df_pages.replace('/', 'homepage', inplace=True)
    
    # Split the url by the first '/' and expand to two columns
    df_pages = df_pages.str.split('/', n=1, expand=True)
    
    # Change the columns names
    df_pages.columns = ['lesson', 'lesson_detail']

    # Concat the lesson columns to the original dataframe
    df = pd.concat([df, df_pages], axis=1)

    # Drop the column page_accessed
    df.drop(columns=['page_accessed', 'lesson_detail'], inplace=True)

    # Handle missing values
    df.cohort_id.fillna(0, inplace=True)
    df.name.fillna('zero', inplace=True)
    df.program_id.fillna(0, inplace=True)
    df.lesson.fillna('homepage', inplace=True)
    df.start_date.fillna(pd.Timestamp('2018-01-26 09:55:03'), inplace=True)
    df.end_date.fillna(pd.Timestamp('2020-11-02 16:48:47'), inplace=True)

    return df