## BQ Import
'''
Functions for interfacing with BQ and running queries remotely.
'''

#%% packages
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas as pd
import pandas_gbq

from preamble import *

#%% params
credentialPath = "credentials/netspark-database-8cc84356c3ce.json"
credentials = service_account.Credentials.from_service_account_file(
    credentialPath)
project_id = "netspark-database"
client = bigquery.Client(credentials=credentials, project=project_id)


#%% bq import - df to loading table.
def bqImport(df, info, schema):
    '''
    Loads pandas df into BQ.
    doc - https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.to_gbq.html
    Parameters:
        df: dataframe, the import data.
        info: series, relevant slice from the master list.
        schema: list of dicts.
    '''    
    groupName='load.'
    table = groupName+info.LoadingTable
    
    pandas_gbq.to_gbq(
        df, 
        table, 
        project_id="netspark-database", 
        table_schema=schema,
        if_exists='replace',
        credentials=credentials
        )

#%% bqQuery - loading table to long-term.
def bqQuery(queryText):
    '''
    Runs queryText in BQ.
    It's possible to retrieve the query results, but I have been getting dead kernels.
    Parameters:
        queryText: string, text of query.
    '''
    job = client.query(queryText)
    job.result()
    
    #- possible output
    #output.to_dataframe(create_bqstorage_client=False)  
    
    return job.state

def bq_query_from_file(queryPath):
    '''
    Runs a query from a local file.    
    Calls bqQuery().
    Can take 'info' as argument.
    Parameters:
        qp - string OR series (overloaded), provides path of query file (query path).
        
    '''
    qp = queryPath
    
    if type(qp)==pd.Series:
        qp = queryFolder+qp.QueryPath
        
    with open(qp, "r", encoding="utf-8") as f:
        query = f.read()
        
    res = bqQuery(query)
        
    return res     
