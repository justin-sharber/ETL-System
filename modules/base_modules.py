## Base modules
'''
Wrapper for loading module base - which is most modules in the sysetm.  
Primarily used by the prep_file module.
'''

#- general modules
from preamble import *
from detect_files import *
from general_readers import *
from read_data_key import *
from export_df import export
from upload import upload
from bq_import import *
print('General modules loaded.')

#- control modules
from standardize_columns import *
from data_controls import *
from drop_delimiters import *
from clean_columns import *
from supplement_data import supplementData
print('Control modules loaded.')

#- sql
from make_query import makeUpsertQuery

#- misc
from miscFunctions import *

#%% preload
from load_master_list import *
masterList.shape

