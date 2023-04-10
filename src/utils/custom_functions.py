# imports
import os
import pandas as pd
from pandas_profiling import ProfileReport

def generate_descriptive_analysis(df : pd.DataFrame, output_filename: str) :
    """This function will create a HTML report describing the dataframe submitted.
    Careful, this can be time-consuming.

    Args:
        df (pd.DataFrame): _description_
    """

    # Generate the ProfileReport
    profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

    # Save the report as an HTML file
    path_to_save = os.path.join(r"./reports", output_filename + ".html")
    try:
        profile.to_file(path_to_save)
    except: 
         profile.to_file('/Users/clement/Desktop/ULB/Doctorat/ECARES M2/Advanced topics in Economics/Project/gravity_trade/data' + output_filename)

def label_sent_analysis(entry):
    
    if entry > 0:
        return 1
    else :
        return 0

def label_sent_analysis(entry):
    """This function check if a tweet is positive, or not. 
    If positive, it returns 1.
    Args:
        entry (string): score
    Returns:
        Boolean: 1 if positive, 0 otherwise.
    """
    if entry > 0:
        return 1
    else :
        return 0

def label_political_entity(entry):
    """This function check if a tweet is positive, or not. 
    If positive, it returns 1.
    Args:
        entry (string): score
    Returns:
        Boolean: 1 if positive, 0 otherwise.
    """
    if not entry:
        return 0
    else :
        return 1

def prepare_gdp_file(path_to_data, gdp_filename): 
    """Refactofing file.

    Args:
        path_to_data (_type_): _description_
        gdp_filename (_type_): _description_
    """
    gdp1 = pd.read_csv(os.path.join(path_to_data, gdp_filename))
    gdp1 = gdp1[gdp1["Series Name"] == "GDP (current US$)"]
    gdp1.rename(columns=mapping_years, inplace=True)
    gdp1 = gdp1.drop(columns=['Country Name','Series Name', 'Series Code'])
    gdp1 = gdp1.set_index('Country Code')
    gdp1 = gdp1.stack().reset_index()
    gdp1.rename(columns = {'level_1':'year', 0:'gdp'}, inplace=True)
    gdp1['Key'] = gdp1['Country Code'] + '_' + gdp1['year'].astype(str)
    
    return gdp1