# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
#   "requests",
#   "load_dotenv",
#   "tabulate"
#  ]
# ///

import requests
import os
import sys
import re
import pandas as pd
from dotenv import load_dotenv
import subprocess


load_dotenv()

#global variables
column_classify = []

api_key = os.environ["AIPROXY_TOKEN"] 
response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Need you to analyse a csv file and provide its statistical information"},
            ]
        }
    )
result = response.json()

def load_csv(file_path):
    """Load a CSV file into a pandas DataFrame."""
    df = pd.read_csv(file_path,encoding='latin-1')
    return df

def analyze_data(df,file_name):
    """Perform basic analysis on the DataFrame and create a story."""
    shape = df.shape
    columns = df.columns.tolist()
    description = df.describe()
    null_values = df.isnull().sum()
    numerical_columns = len(df.select_dtpes(include="float"))
    
    story = f"# Data Analysis Report\n\n"
    story += f"## Dataset Information\n\n"
    story += f"The dataset {file_name} contains {shape[0]} rows and {shape[1]} columns.\n\n"
    story += f"### Columns:\n\n"
    for column in columns:
        story += f"- {column}\n"
    story += f"## Dataset Classification\n\n"
    story += f"The input file contains {numerical_columns} numerical columns and {shape[1]-numerical_columns} categorical columns. "
    story += f"Based on the column names at very high level identified that file might contain: "         
    story += f"\n".join([f"* {item}" for item in column_classify])
    story += f"\n## Summary Statistics\n\n"
    story += f"{description.to_markdown()}\n\n"
    story += f"## Missing Values\n\n"
    for column, num_missing in null_values.items():
        story += f"- {column}: {num_missing} missing values\n"
    
    return story

def save_markdown(file_path, content):
    REPO_OWNER = "Nandhini-Ammaiappan"
    repo_path = "/mnt/c/Users/Nandhini/OneDrive/Documents/GitHub/Project-2---Automated-Analysis/"
    remote_url = "https://github.com/{REPO_OWNER}/{REPO_NAME}.git"

    folder_name = file_path[0].split('.')

    os.chdir(repo_path)
    subprocess.run(["git", "config", "--global","user.name", REPO_OWNER])
    if not os.path.exists(folder_name[0]):
        os.makedirs(folder_name[0])
    repo_path += folder_name[0]
    readme_file = os.path.join(repo_path, "README.md")
    with open(readme_file, "w") as f:
        f.write(content)
    subprocess.run(["git", "add", readme_file])
    subprocess.run(["git", "commit", "-m", "Add new"])
    subprocess.run(["git", "push", "-u", "origin", "main"])

def validation():
    
    # Validates if the the csv file is provided or not
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <csv_filename>")
        sys.exit(1)
        
    #validates if the csv file exists in the specified path 
    if not os.path.isfile(file_path):
        print(f"The file '{file_path}' does not exist.")
        sys.exit(1)

def request_llm (request_text):
    response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": request_text},
            ]
        }
    )
    result = response.json()

    print(result)
    

def data_classification(df):
    
    #grouping the columns based on the header names - this is only sample list
    geographical = ['town','city','city/town','region','district','state','country','pincode','zipcode','latitute','longitude','lat','log']
    timeseries = ['seconds','minutes','hour','date','start','end','timestamp','time','month','year','week']
    moneyseries = ['price','cost','profit','loss','expense','expenditure','debit','credit','p/l','gdp','capita','income']
    others = ['name','ratings','overall','id','product','title']

    #list defined to hold the columns name respectively
    geographical_columns = []
    moneyseries_columns = []
    timeseries_columns = []
    others_columns = []
    unclassified_columns =[]

    #setting flags to false to idetify the high level classification
    geographical_data_present = timeseries_data_present = moneyseries_data_present = others_data_present = False
    
    column_classify = []
    #tries to classify each column present in the input file
    for column_name in df.columns:
        part_names = column_name.split(' ')
        for parts in part_names:
            if parts.lower() in geographical:
                geographical_data_present = True
                geographical_columns += [column_name]
            if parts.lower() in timeseries:
                timeseries_data_present = True
                timeseries_columns += [column_name]
            if parts.lower() in moneyseries:
                moneyseries_data_present = True
                moneyseries_columns += [column_name]
            if parts.lower() in others:
                others_data_present = True
                others_columns += [column_name] 
        if geographical_data_present:
            column_classify += ['Geographical']
        if moneyseries_data_present:
            column_classify += ['Financial']
        if timeseries_data_present:
            column_classify += ['Time series'] 
            
        if not (geographical_data_present or timeseries_data_present or moneyseries_data_present or others_data_present):
            unclassified_columns += [column_name] 
        
        column_name_list = ', '.join(unclassified_columns)
    
    #use LLM to classify the unclassified columns
    request_llm('Classify each of the following ' + column_name_list + 'as geographical, time,money or others.')


def validation():

    # Validates if the the csv file is provided or not
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <csv_filename>")
        sys.exit(1)
        
    #validates if the csv file exists in the specified path 
    if not os.path.isfile(sys.argv[1]):
        print(f"The file '{sys.argv[1]}' does not exist.")
        sys.exit(1)

def main():

    #this function is to validate the input file
    validation()        
    
    #extract only the filename from the argument 
    file_name = re.split(r'/\[a-zA-Z0-9]*.csv',sys.argv[1])
    
    #load the contents of the input file into dataframe
    df = load_csv(sys.argv[1])
    
    #function to classify the contents of the input file based on column names
    data_classification(df)
    
    #extract only 1/10 records from the input as sample for analysis
    sample_df = df.head(len(df)//10).to_json(orient='records')
    
    analysis_story = analyze_data(df,file_name)
    save_markdown(file_name, analysis_story)
    print("Analysis complete. Check README.md for the results.")

if __name__ == "__main__":
    # this is the beginning
    main()