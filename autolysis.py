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
import pandas as pd
from dotenv import load_dotenv
import subprocess


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
    REPO_OWNER = "Nandhini-Ammaiappan"
    repo_path = "/mnt/c/Users/Nandhini/OneDrive/Documents/GitHub/Project-2---Automated-Analysis/"
    remote_url = "https://github.com/{REPO_OWNER}/{REPO_NAME}.git"

    folder_name = file_path.split('.')

    os.chdir(repo_path)
    subprocess.run(["git", "config", "--global","user.name", REPO_OWNER])
    if not os.path.exists(folder_name[0]):
        os.makedirs(folder_name[0])
    repo_path += folder_name[0]
    placeholder_file = os.path.join(repo_path, ".gitkeep")
    with open(placeholder_file, "w") as f:
        f.write("")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Add new"])
    readme_file = os.path.join(repo_path, "README.md")
    with open(readme_file, "w") as f:
        f.write(content)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Add new"])
    subprocess.run(["git", "remote", "add", "origin", remote_url])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "push", "-u", "origin", "main"])

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