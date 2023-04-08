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
    profile.to_file(path_to_save)

