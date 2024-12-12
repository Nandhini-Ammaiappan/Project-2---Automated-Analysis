# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
#   "requests",
#   "load_dotenv",
#   "tabulate"
# ]
# ///

import requests
import os
import sys
import pandas as pd
import base64
from dotenv import load_dotenv
from github import Github

load_dotenv()

api_key = os.environ["AIPROXY_TOKEN"] 
'''response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "How do I use a proxy with ChatGPT?"},
            ]
        }
    )
result = response.json()
print(result)
'''
def load_csv(file_path):
    """Load a CSV file into a pandas DataFrame."""
    df = pd.read_csv(file_path,encoding='latin-1')
    return df

def analyze_data(df,fn):
    """Perform basic analysis on the DataFrame and create a story."""
    shape = df.shape
    columns = df.columns.tolist()
    description = df.describe()
    null_values = df.isnull().sum()
    
    story = f"# Data Analysis Report\n\n"
    story += f"## Dataset Information\n\n"
    story += f"The dataset {fn} contains {shape[0]} rows and {shape[1]} columns.\n\n"
    story += f"### Columns:\n\n"
    for column in columns:
        story += f"- {column}\n"
    story += f"\n## Summary Statistics\n\n"
    story += f"{description.to_markdown()}\n\n"
    story += f"## Missing Values\n\n"
    for column, num_missing in null_values.items():
        story += f"- {column}: {num_missing} missing values\n"
    
    return story

def save_markdown(file_path, content):
    """Save the analysis content to a Markdown file."""
    GITHUB_TOKEN = os.environ["GITHUB"]
    REPO_OWNER = "Nandhini-Ammaiappan"
    REPO_NAME = "Project-2---Automated-Analysis/{file_path}"
    NEW_FOLDER_PATH = "file_path"

    # Connect to GitHub
    g = Github(GITHUB_TOKEN)
    
    # Get the repository
    repo = g.get_user().get_repo(REPO_NAME)

    repo.create_file("README.md", "Create README.md", content)
    '''   url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{NEW_FOLDER_PATH}/README.md'

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    data = {
        'message': 'Create new folder',
        'content': file_content_encoded
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        print('Folder created successfully.')
    else:
        print('Failed to create folder:', response.json())

    '''   
    #with open(file_path, 'w') as f:
    #   f.write(content)

def main():
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <csv_filename>")
        sys.exit(1)

    csv_filename = sys.argv[1]
    df = load_csv(csv_filename)
    print(sys.argv[1])
    analysis_story = analyze_data(df,csv_filename)
    save_markdown(csv_filename, analysis_story)
    print("Analysis complete. Check README.md for the results.")

if __name__ == "__main__":
    main()