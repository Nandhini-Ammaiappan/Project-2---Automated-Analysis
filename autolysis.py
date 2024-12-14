# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
#   "requests",
#   "load_dotenv",
#   "tabulate",
#   "matplotlib"
#  ]
# ///

import requests
import os
import sys
import re
import pandas as pd
from dotenv import load_dotenv
import subprocess
import matplotlib.pyplot as plt


#global list defined to hold the columns name respectively
global df
geographical_columns = []
moneyseries_columns = []
timeseries_columns = []
others_columns = []
unclassified_columns = []
numerical_columns = []
categorical_columns = []

load_dotenv()

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

function_descriptions_multiple = [
    {
        "name": "get_plot_information",
        "description": "To get details on the plot/graph that can be drawn from the data provided",
        "parameters": {
            "type": "object",
            "properties": {
                "Plot Type": {
                    "type": "string",
                    "description": "The name of the plot, e.g. Bar, Line",
                },
                "X-axis": {
                    "type": "string",
                    "description": "The name of the column that can used as x axis e.g. language",
                },
                "Y-axis": {
                    "type": "string",
                    "description": "The name of the column that can used as y axis e.g. rating",
                },
            },
            "required": ["Plot Type", "X-axis", "Y-axis"],
        },
    },
    {
        "name": "draw_the_plot",
        "description": "To draw the plot/graph using the data received",
        "parameters": {
            "type": "object",
            "properties": {
                "Plot Type": {
                    "type": "string",
                    "description": "The name of the plot, e.g. Bar, Line",
                },
                "X-axis": {
                    "type": "string",
                    "description": "The name of the column that can used as x axis e.g. language",
                },
                "Y-axis": {
                    "type": "string",
                    "description": "The name of the column that can used as y axis e.g. rating",
                },
            },
            "required": ["Plot Type", "X-axis", "Y-axis"],
        },
    },
]

def get_brief_description(sample_data):
    # Example output returned from an API or database
    text_message = {
        "message": sample_data
    }
    return json.dumps(plot_info)

def get_plot_information():
    # Example output returned from an API or database
    plot_info = {
        "Plot Type": plot_name,
        "X-axis": column_name_x,
        "Y-axis": column_name_y,
    }
    print(json.dumps(plot_info))
    return json.dumps(plot_info)

def draw_the_plot():
    # Example output returned from an API or database
    plot_data = {
        "Plot Type": plot_name,
        "X-axis": column_name_x,
        "Y-axis": column_name_y,
    }
    return json.dumps(plot_data)

def ask_and_reply(prompt,sample_data):
    """Give LLM a given prompt and get an answer."""
    response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt+"\n"+sample_data},
            ],
        "functions": function_descriptions_multiple,
        "function_call": "auto",
        }
    )
  
    output = response.json()
    print(output)
    return output

def plot_graph():
    #to plot grap based on the columns

    # Create a bar chart
    for y in numerical_columns:
        for x in categorical_columns:
            plt.bar(x,y, color="skyblue")

            # Add title and labels
            plt.title('Sample BarChart')
            plt.xlabel(x)
            plt.ylabel(y)

            plt.savefig('{x}.png')
            # Display the chart
            plt.show()

def load_csv(file_path):
    """Load a CSV file into a pandas DataFrame."""
    global df
    df = pd.read_csv(file_path,encoding='latin-1')
    return df

def analyze_data(file_name,classified_list,initial_analyis,statistical_analysis):
    """Perform basic analysis on the DataFrame and create a story."""
    global df
    shape = df.shape
    columns = df.columns.tolist()
    description = df.describe()
    null_values = df.isnull().sum()
    numerical_columns = len(df.select_dtypes(include="float").columns)
    
    story = f"# Data Analysis Report\n\n"
    story += f"## Dataset Information\n\n"
    story += f"{initial_analyis}"
    story += f"\nThe dataset {file_name} contains {shape[0]} rows and {shape[1]} columns.\n\n"
    story += f"### Statistical Details:\n\n"
    story += f'{statistical_analysis}'
    story += f"\n\n## Dataset Classification\n\n"
    story += f"The input file contains {numerical_columns} numerical columns and {shape[1]-numerical_columns} categorical columns. "
    '''if len(classified_list) > 0:
        story += f"Based on the column names at very high level identified that file might contain: "         
        story += f"\n".join([f"* {item}" for item in classified_list])
    '''
    story += f"### Plot Information:\n\n"
    #story += f'{plot_suggestion}'
    story += f"\n## Summary Statistics\n\n"
    story += f"{description.to_markdown()}\n\n"
    story += f"## Missing Values\n\n"
    for column, num_missing in null_values.items():
        if num_missing > 0:
            story += f"- {column}: {num_missing} missing values\n"
    
    return story

def save_markdown(file_name, content):
    #this function writes the narratives to current working folder locally as well commits to the project folder in git
    
    #standard variables defined with the folder definition
    REPO_OWNER = "Nandhini-Ammaiappan"
    REPO_NAME = "Project-2---Automated-Analysis"
    repo_path = "/mnt/c/Users/Nandhini/OneDrive/Documents/GitHub/Project-2---Automated-Analysis/"
    remote_url = "https://github.com/Nandhini-Ammaiappan/Project-2---Automated-Analysis.git"

    #retrieves only the filename to create the folder in git
    file_name_only,extension = file_name.split('.')
    
    #gets the current folder in the local drive
    folder_path = os.getcwd() 

    #checks if the local folder/directory is already present, else creates one
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    #sets path to current working directory
    os.chdir(folder_path)

    #writes the narrative to the local README
    local_file = os.path.join(folder_path,"README.md")
    with open(local_file, "w") as file:
        file.write(content)
    
    #defines the repository path in the github, creates folder if not present
    repo_folder_path = os.path.join(repo_path, file_name_only)
    os.makedirs(repo_folder_path, exist_ok=True)
    
    #writes the narrative to the github folder README
    readme_file = os.path.join(repo_folder_path, "README.md")
    with open(readme_file, "w") as file:
        file.write(content)
    try:
        #subprocess executed to push the README from github to git repository and commit the same
        subprocess.run(["git", "config", "--global","user.name", REPO_OWNER],check=True)
        subprocess.run(["git", "add", repo_folder_path])
        subprocess.run(["git", "add", readme_file],check=True)
        subprocess.run(["git", "commit", "-m", "Add README file"],check=True)
        #subprocess.run(["git","remote","add","origin",remote_url],check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"],check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def validation():

    # Validates if the the csv file is provided or not
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <csv_filename>")
        sys.exit(1)
        
    #validates if the csv file exists in the specified path 
    if not os.path.isfile(sys.argv[1]):
        print(f"The file '{sys.argv[1]}' does not exist.")
        sys.exit(0)


def request_llm (data,request_text):
    response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}","Content-Type":"application/json"},
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{request_text}\n{data}"}
            ]
        }
    )

    if response.status_code == 200:
        return(response.json()['choices'][0]['message']['content'])
    else:
        return(f"Unable to get response from LLM - {response.status_code}")
    
    
def data_classification():
    
    global df, unclassified_columns, geographical_columns,others_columns,timeseries_columns, moneyseries_columns
    #grouping the columns based on the header names - this is only sample list
    geographical = ['town','city','city/town','region','district','state','country','pincode','zipcode','latitute','longitude','lat','log']
    timeseries = ['seconds','minutes','hour','date','start','end','timestamp','time','month','year','week']
    moneyseries = ['price','cost','profit','loss','expense','expenditure','debit','credit','p/l','gdp','capita','income']
    others = ['name','ratings','overall','id','product','title']
    column_classification = []
    #setting flags to false to idetify the high level classification
    geographical_data_present = timeseries_data_present = moneyseries_data_present = others_data_present = False
    
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
            column_classification += ['Geographical']
        if moneyseries_data_present:
            column_classification += ['Financial']
        if timeseries_data_present:
            column_classification += ['Time series'] 
            
        if not (geographical_data_present or timeseries_data_present or moneyseries_data_present or others_data_present):
            unclassified_columns += [column_name] 
        
        numerical_columns = df.select_dtypes(include="float").columns
        categorical_columns = df.select_dtypes(exclude ="float").columns
        column_name_list = ', '.join(unclassified_columns)
    
    #use LLM to classify the unclassified columns
    #request_llm('Classify each of the following ' + column_name_list + 'as geographical, time,money or others.')
    return (column_classification)

def main():

    global df
    #this function is to validate the input file
    validation()        
    
    #extract only the filename from the argument 
    file_name = os.path.basename(sys.argv[1])
    
    #load the contents of the input file into dataframe
    df = load_csv(sys.argv[1])
    
    #function to classify the contents of the input file based on column names
    classified_list = data_classification()
    
    #extract only 1/10 records from the input as sample for analysis
    sample_data = df.head(len(df)//10).to_json(orient='records')
    
    #scenario 1
    '''user_prompt = "Suggest what this report contains"
    initial_analysis = ask_and_reply(user_prompt,sample_data)
    
    #scenario 2
    user_prompt = "Provide statistical details based on the data provided"
    statistical_analysis = ask_and_reply(user_prompt,sample_data)
'''
    #scenario 3
    '''user_prompt = "Suggest what plots can be created using this report and provide its axis details"
    plot_suggestion = ask_and_reply(user_prompt,sample_data)
    print(plot_suggestion)
'''

    '''initial_analysis = request_llm(sample_data,"Suggest what this report contains")
    statistical_analysis = request_llm(sample_data,"Provide statistical details based on the data provided")
    #plot_suggestion = request_llm(sample_data,"Suggest what plots can be created using this report and provide its axis details")
    analysis_story = analyze_data(file_name,classified_list,initial_analysis,statistical_analysis)
    '''
    analysis_story = "Temp data1"
    save_markdown(file_name, analysis_story)
    print("Analysis complete. Check README.md for the results.")

if __name__ == "__main__":
    # this is the beginning
    main()