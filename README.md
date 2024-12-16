#Autolysis: Project 2 of IITM BS Data Science (Diploma)

##Overview
This project is to intended for students to learn and explore on the building of application which can use LLMs' for their needs. 

##Case study 
Any csv file which is provided as input should be analyzed and provide a brief description of it content. Also should produce more advanced statistical information with visual aids like plots. 

##Key Features
1. Data loading and validation
2. Data analysis using multiple features of python and LLM
3. Creating plots using analysed data
4. Creating work flow using function calling of LLM
5. Creating summary of the analsyis and storing it in README

##Technical Requirements
1. UV - Python Package MAnager
2. OpenAI - For interacting with LLM
3. Pandas - For dataframe and handling data received from input csv files
4. Seaborn & Matplotlib - For ploting charts
   
##Execution
uv run autolysis.py <input.csv>

##Output:
Narratives - /<input>/README.md
Plots - /<input>/*.png
