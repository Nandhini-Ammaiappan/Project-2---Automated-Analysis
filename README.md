# Data Analysis Report

## Dataset Information

This report seems to be a comprehensive catalog of movie and series reviews, showcasing various titles from different languages, genres, and release dates. Here’s a breakdown of what the report likely contains:

### Structure and Contents

1. **Date of Review**: Each entry includes the date the movie or series was reviewed.
   
2. **Language**: Mentions the language of the movie or series (e.g., Tamil, Telugu, English, Hindi, Japanese, etc.).

3. **Type**: Indicates whether the entry is a movie or a series.

4. **Title**: Lists the name of the movie or series.

5. **Actors Involved**: Names the lead actors or contributors involved in the movie or series. Some titles are marked "null" if no specific actors are mentioned.

6. **Overall Rating**: A numeric score representing the reviewer's overall impression of the movie or series, likely on a scale of 1 to 5 (or possibly 1 to 10).

7. **Quality Rating**: A numeric score reflecting the technical and artistic quality of the movie or series.

8. **Repeatability**: A numeric score indicating the likelihood of the reviewer watching the movie or series again. A lower score might suggest it’s less likely to be rewatched, while a higher score indicates enjoyment.

### Analysis 

- **Performance Trends**: The report suggests patterns in the performance of different movies, such as which actors frequently appear in higher-rated productions.
- **Cultural Insights**: With entries in multiple languages, the report could provide insight into regional cinematic tastes and trends.
- **Movie/Series Popularity**: An analysis can be conducted on which titles received higher ratings and are more favored by viewers.
- **Quality Control**: Quality ratings can reveal insights into production values, directing style, and overall viewer satisfaction.

### Potential Uses

- **Viewer Guidance**: This report can serve as a guide for viewers looking for recommendations based on ratings and repeatability scores.
- **Industry Analysis**: Producers and filmmakers may analyze the data to understand what genres or actors are currently successful.
- **Market Trends**: Could help in assessing market demand for various types of content across different languages.

### Summary 

Overall, this report serves as a valuable database of feedback on a vast array of films and series, offering insights into viewer opinions and preferences in the entertainment industry. It could be beneficial for film aficionados, industry professionals, and casual movie-goers alike.The dataset media.csv contains 2652 rows and 8 columns.

### Columns:

- date
- language
- type
- title
- by
- overall
- quality
- repeatability
## Dataset Classification

The input file contains 0 numerical columns and 8 categorical columns. Based on the column names at very high level identified that file might contain: * Time series
* Time series
* Time series
* Time series
* Time series
* Time series
* Time series
* Time series
## Summary Statistics

|       |    overall |     quality |   repeatability |
|:------|-----------:|------------:|----------------:|
| count | 2652       | 2652        |     2652        |
| mean  |    3.04751 |    3.20928  |        1.49472  |
| std   |    0.76218 |    0.796743 |        0.598289 |
| min   |    1       |    1        |        1        |
| 25%   |    3       |    3        |        1        |
| 50%   |    3       |    3        |        1        |
| 75%   |    3       |    4        |        2        |
| max   |    5       |    5        |        3        |

## Missing Values

- date: 99 missing values
- language: 0 missing values
- type: 0 missing values
- title: 0 missing values
- by: 262 missing values
- overall: 0 missing values
- quality: 0 missing values
- repeatability: 0 missing values
