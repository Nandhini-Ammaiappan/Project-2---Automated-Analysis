# Data Analysis Report

## Dataset Information

This report appears to be a compilation of movie and television series reviews based on various attributes. Here's a breakdown of the contents you can expect to find in the report:

1. **Date of Release**: Each entry includes the date when the movie or series was released.

2. **Language**: The primary language of the movie or series (e.g., Tamil, Telugu, Hindi, English, etc.).

3. **Type**: The classification of the content, primarily as "movie" or "series".

4. **Title**: The name of the movie or series.

5. **Cast/Production Team**: Names of key figures associated with the work, such as actors or directors.

6. **Overall Rating**: A numeric score reflecting the reviewer’s overall impression, usually on a scale from 1 to 5.

7. **Quality Rating**: A separate score focused on the production quality, also likely on the same scale.

8. **Repeatability Rating**: An indication of whether the reviewer would watch the content again, which could be on a similar numeric scale.

### Summary of Insights:
- **Highest Rated Content**: Titles like "Meiyazhagan," "Attack on Titan," "Doctor," and "Ponniyin Selvan 2" stand out with high ratings.
- **Diversity in Genres**: The report covers a wide range of genres including action, drama, romance, and fantasy, across multiple languages.
- **Viewer Preferences**: Repeatability ratings can indicate viewer interest in rewatching certain titles, providing insight into audience favorites.
- **Quality Assessment**: The quality ratings serve to help readers discern the technical and artistic merits of the movies and series, separate from personal enjoyment.

Overall, the report serves as a comprehensive review guide, helping readers evaluate the recent cinematic landscape across various languages and styles.The dataset media.csv contains 2652 rows and 8 columns.

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
