# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
#   "requests",
#   "load_dotenv",
#   "tabulate",
#   "matplotlib",
#   "seaborn"
#  ]
# ///

#import libraries for processing
import json
import os
import requests
import seaborn as sns
import subprocess
import sys
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

#setting API key for API request 
api_key = os.environ["AIPROXY_TOKEN"]
    
#-------------------------------------------------------------------------------------------------------------------------------------#
#   function_descriptions_multiple - setting the different function calls for API
#-------------------------------------------------------------------------------------------------------------------------------------#
function_descriptions_multiple = [
    {
        "name": "get_brief_description",
        "description": "With help of file name and listed column names provide complete description on what type of data held in the file",
        "parameters": {
            "type": "object",
            "properties": {
                "insights": {
                    "type": "string",
                    "description": "To provide a complete description of the file based on file and column names",
                    "items":{"type":"string"}
                }
            },
            "required": ["description"],
        },
    },
    {
        "name": "get_column_classification",
        "description": "To classify the columns based on the column names received like categorical,numerical,timeseries,boolean",
        "parameters": {
            "type": "object",
            "properties": {
                "Categorical": {
                    "type": "array",
                    "description": "List all columns that are categorical in nature",
                    "items":{"type":"string"}
                },
                "Numerical": {
                    "type": "array",
                    "description": "List all columns that are numerical",
                     "items":{"type":"string"}
                },
                "Timeseries": {
                    "type": "array",
                    "description": "List all columns that contain year,month, date, time etc.,",
                     "items":{"type":"string"}
                },
                "Boolean": {
                    "type": "array",
                    "description": "List all columns that only two values like True or False",
                     "items":{"type":"string"},
                },
                "Others":{
                    "type":"array",
                    "description": "List all remaining columns from the list which can not be classified",
                    "items":{"type":"string"}
                }
            },
            "required": ["Categorical", "Numerical", "Timeseries","Boolean","Others"],
        },
    },
    {
        "name": "get_plot_information",
        "description": "Get plot type along with the axis details based on the column names",
        "parameters": {
            "type": "array",
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
            "type": "array",
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

#-------------------------------------------------------------------------------------------------------------------------------------#
#   get_plot_information - gets the different plots that can be drawn from the file
#-------------------------------------------------------------------------------------------------------------------------------------#
def get_plot_information(columns):
    
    plot_details = ask_and_reply("Get plot types along with axis information based on following columns : " + str(columns))
    return(plot_details)
    
#-------------------------------------------------------------------------------------------------------------------------------------#
#   draw_the_plot - function to draw three most important plots/graphs
#-------------------------------------------------------------------------------------------------------------------------------------#
def draw_the_plot(df,file_name,plot_details):
    
    #assign to local variables
    type = plot_details["Plot Type"]
    xaxis=plot_details["X-axis"]
    yaxis=plot_details["Y-axis"]
    
    #plot creation
    plt.figure(figsize=(10,6))
    sns.barplot(data=df,x=xaxis,y=yaxis)
    
    title = type + " chart"
    #set plot title and labels
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    
    file_name_only,extension = file_name.split(".")
    
    #save the plot as PNG file
    plt.savefig(file_name_only + "/" + type + "_plot.png")

    #gets the current folder in the local drive
    folder_path = os.getcwd() 

    #checks if the local folder/directory is already present, else creates one
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    #sets path to current working directory
    os.chdir(folder_path)
    #save the plot as PNG file in local folder
    plt.savefig("./" + type + "_plot.png")

#-------------------------------------------------------------------------------------------------------------------------------------#
#   ask_and_reply - common function to get the response from LLM
#-------------------------------------------------------------------------------------------------------------------------------------#
def ask_and_reply(prompt):
    
    response = requests.post("https://api.openai.com/v1/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role":"system","content":"You are a helpful assistant"},
            {"role": "user", "content": prompt},
            ],
        "functions": function_descriptions_multiple,
        "function_call": "auto",
        }
    )
    
    if response.status_code == 200:
        output = response.json()['choices'][0]['message']['function_call']['arguments']
        print(output)
        structured_output = json.loads(output)
        return structured_output
    else:
        print(f"Unable to get response from LLM - {response.status_code}")
        return(f"Unable to get response from LLM - {response.status_code}")

#-------------------------------------------------------------------------------------------------------------------------------------#
#   build_narratives - this function builds the narratives for writing into README
#-------------------------------------------------------------------------------------------------------------------------------------#
def build_narratives(file_name,df,description,column_types):
    
    shape = df.shape
    columns = df.columns.to_list()

    stats_description = df.describe()
    null_values = df.isnull().sum()
    file_name_only,extension = file_name.split(".")
    
    #Brief description of the files.
    story = f"# Description of the file\n\n"
    story += f"\n{file_name.upper()} is used as input for the analysis. This file contains {shape[0]} rows and {shape[1]} columns.\n"
    story += f"{description}\n"
    story += f"{column_types}\n\n"
    
    #statistical details
    story += f"### Statistical Details:\n\n"
    #story += f'{statistical_analysis}'
    
    story += f"\n## Summary Statistics\n\n"
    story += f"{stats_description.to_markdown()}\n\n"
    
    story += f"## Missing Values\n\n"
    for column, num_missing in null_values.items():
        if num_missing > 0:
            story += f"- {column}: {num_missing} missing values\n"
    
    story += f"## Graphical Representation of data\n\n"
    png_files = [f for f in os.listdir(file_name_only) if f.endswith('.png')] 
    for png_file in png_files: 
        story += f'![{png_file}]({png_file})\n'
   
    return story

#-------------------------------------------------------------------------------------------------------------------------------------#
#   validation - this function validates the input file
#-------------------------------------------------------------------------------------------------------------------------------------#
def validation():

    # Validates if the the csv file is provided or not
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <csv_filename>")
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"The file '{sys.argv[1]}' does not exist.")
        sys.exit(0)

#-------------------------------------------------------------------------------------------------------------------------------------#
#   load_csv - this function loads the csv file after respective encoding to dataframe
#-------------------------------------------------------------------------------------------------------------------------------------#
def load_csv(file_path):
    
    df = pd.read_csv(file_path,encoding='latin-1')
    return df

#-------------------------------------------------------------------------------------------------------------------------------------#
#   save_markdown - this function writes the narrative content into README and commits to GIT repository
#-------------------------------------------------------------------------------------------------------------------------------------#
def save_markdown(file_name, content):
    
    #standard variables defined with the folder definition
    REPO_OWNER = "Nandhini-Ammaiappan"
    repo_path = "/mnt/c/Users/Nandhini/OneDrive/Documents/GitHub/Project-2---Automated-Analysis/"
    
    #retrieves only the filename to create the folder in git
    file_name_only,extension = file_name.split('.')
    
    #gets the current folder in the local drive
    folder_path = os.getcwd() 

    #checks if the local folder/directory is already present, else creates one
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    #sets path to current working directory
    os.chdir(folder_path)

    #writes the narrative to the current folder
    with open("README.md", "w") as file:
        file.write(content)
    
    #defines the repository path in the github, creates folder if not present
    repo_folder_path = os.path.join(repo_path, file_name_only)
    if not os.path.exists(repo_folder_path):
        os.makedirs(repo_folder_path, exist_ok=True)
    os.chdir(repo_folder_path)
    
    #writes the narrative to the github folder README
    readme_file = os.path.join(repo_folder_path, "README.md")
    with open(readme_file, "w") as file:
        file.write(content)
    
    #subprocess executed to push the README from github to git repository and commit the same
    subprocess.run(["git", "config", "--global","user.name", REPO_OWNER],check=True)
    subprocess.run(["git", "add", repo_folder_path],check=True)
    subprocess.run(["git", "add", readme_file],check=True)
    subprocess.run(["git", "commit", "-m", "Add README file"])
    subprocess.run(["git", "push", "-u", "origin", "main"],check=True)

#-------------------------------------------------------------------------------------------------------------------------------------#
#   file_description - this function request LLM to provide description of the file
#-------------------------------------------------------------------------------------------------------------------------------------#
def file_description(file_name,columns):
           
    #sends the file name and all its columns to brief dscription of the file
    insights = ask_and_reply("Provide brief description of the file {file_name} having following columns : " + str(columns))
    return(insights['insights'])
    
#-------------------------------------------------------------------------------------------------------------------------------------#
#   data_classification - this function groups the columns based 
#-------------------------------------------------------------------------------------------------------------------------------------#
def data_classification(columns):
    
    boolean_columns = categorical_columns = numerical_columns = timeseries_columns = unclassified_columns = []
    text_list = []
    #sends the column names and request for the classification of the columns
    classification = ask_and_reply("Classify following columns based on their names: " + str(columns))
    
    #populates the classified columns to local list for further processing
    boolean_columns      = classification['Boolean']
    categorical_columns  = classification['Categorical']
    numerical_columns    = classification['Numerical']
    timeseries_columns   = classification['Timeseries']
    unclassified_columns = classification['Others']

    text = "Columns in the file can be grouped into  "
    if len(boolean_columns) > 0:
        text_list += ["boolean"]
    if len(categorical_columns) > 0:
        text_list += ["categorical"]
    if len(numerical_columns) > 0:
        text_list += ["numerical"]
    if len(timeseries_columns) > 0:
        text_list += ["time-series"] 
    
    if len(text_list) > 0:
        return(text + ', '.join(text_list) + '.')
    else:
        return("Unable to classify the columns through LLM")
#-------------------------------------------------------------------------------------------------------------------------------------#
#   main - this is the main function 
#-------------------------------------------------------------------------------------------------------------------------------------#
def main():

    #this function is to validate the input file
    validation()        
    
    #extract only the filename from the argument 
    file_name = os.path.basename(sys.argv[1])
    
    #load the contents of the input file into dataframe
    df = load_csv(sys.argv[1])
    
    #gets the column names of the input file
    columns = df.columns.to_list()

    #to get brief description of the file
    description = file_description(file_name,columns)
    
    #function to classify the contents of the input file based on column names
    column_types = data_classification(columns)
    
    #get plot details
    plot_details = get_plot_information(columns)

    #draw plots for narratives
    plot = draw_the_plot(df,file_name,plot_details)

    #sample data about 1/10th of original data created
    sample_data = df.head(len(df)//10).to_json(orient='records')
    
    #build the narratives in the markdown format
    content = build_narratives(file_name, df, description,column_types)

    #write the narratives into the Git repository
    save_markdown(file_name,content)
    
    print("Analysis complete. Check README.md for the results.")

#-------------------------------------------------------------------------------------------------------------------------------------#
#   Main 
#-------------------------------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    # this is the beginning
    main()