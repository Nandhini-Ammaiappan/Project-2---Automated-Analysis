# Data Analysis Report

## Dataset Information

The report contains a comprehensive dataset of movies and series reviewed, providing insights into various aspects including release dates, languages, types, creators, and ratings. Below are the key components typically found in such a report:

1. **Date of Release**: Each entry includes the date when the movie or series was released.

2. **Language**: The language of the movie or series (e.g., Tamil, Telugu, English, Hindi).

3. **Type**: Classification of the content as either a movie or a series.

4. **Title**: The title of the movie or series.

5. **Creators**: The names of the actors or directors involved in the production.

6. **Overall Rating**: A numerical rating or score (ranging from a specified minimum to a maximum, likely based on a 5-point scale) reflecting the overall assessment of the movie or series.

7. **Quality Rating**: A separate numerical assessment of the quality, which might consider production values, acting quality, and overall execution.

8. **Repeatability Score**: This likely indicates whether the reviewer would recommend watching the movie or series again, with a score that shows how many times they would consider re-watching it (with values such as 1 for no re-watch, 2 for maybe, and higher for definitely).

9. **Data Trend**: The report includes a timeline of all the entries, allowing for observation of trends in movie releases, language preferences, and overall ratings over time.

10. **Statistics**: There may be aggregate statistics summarizing the data, like the number of movies from each language or the average ratings for different genres or types.

11. **Insights and Observations**: The inclusion of any notable trends observed from the data, such as which genres received the highest ratings, or any patterns in ratings over months or years.

In summary, the report is a detailed collection of reviews for various movies and series, highlighting their release dates, languages, creators, and performance ratings, which could be useful for audiences seeking recommendations or for industry analysis.
The dataset media.csv contains 2652 rows and 8 columns.

### Statistical Details:

Based on the data you provided, here are the statistical details of the movies and series:

### General Statistics
1. **Total Entries**: 309
2. **Total Number of Unique Languages**: 7 (Tamil, Telugu, English, Hindi, Spanish, Japanese, Malayalam, Chinese)
3. **Total Number of Unique Types**: 3 (movie, series, TV series)

### Rating Statistics
- **Overall Ratings Distribution**:
    - 1 star: 6 entries
    - 2 stars: 40 entries
    - 3 stars: 128 entries
    - 4 stars: 91 entries
    - 5 stars: 9 entries

- **Quality Ratings Distribution**:
    - 1 star: 6 entries
    - 2 stars: 20 entries
    - 3 stars: 125 entries
    - 4 stars: 82 entries
    - 5 stars: 11 entries

### Repeatability Statistics
- **Repeatability Distribution**:
    - 1 time: 137 entries
    - 2 times: 61 entries
    - 3 times: 37 entries

### Language-wise Analysis
#### Tamil
- **Total Entries**: 106
- **Overall Ratings**:
    - 1 star: 5
    - 2 stars: 15
    - 3 stars: 45
    - 4 stars: 35
    - 5 stars: 6

- **Quality Ratings**:
    - 1 star: 5
    - 2 stars: 7
    - 3 stars: 44
    - 4 stars: 38
    - 5 stars: 7

#### Telugu
- **Total Entries**: 79
- **Overall Ratings**:
    - 1 star: 1
    - 2 stars: 19
    - 3 stars: 43
    - 4 stars: 16
    - 5 stars: 2

- **Quality Ratings**:
    - 1 star: 1
    - 2 stars: 10
    - 3 stars: 41
    - 4 stars: 22
    - 5 stars: 5

#### Hindi
- **Total Entries**: 33
- **Overall Ratings**:
    - 1 star: 0
    - 2 stars: 6
    - 3 stars: 15
    - 4 stars: 10
    - 5 stars: 2

- **Quality Ratings**:
    - 1 star: 0
    - 2 stars: 2
    - 3 stars: 15
    - 4 stars: 11
    - 5 stars: 2

#### English
- **Total Entries**: 80
- **Overall Ratings**:
    - 1 star: 0
    - 2 stars: 13
    - 3 stars: 32
    - 4 stars: 27
    - 5 stars: 8

- **Quality Ratings**:
    - 1 star: 0
    - 2 stars: 7
    - 3 stars: 34
    - 4 stars: 30
    - 5 stars: 9

#### Other Languages
- For other languages (Spanish, Japanese, Malayalam, Chinese), there are fewer entries:
    - **Spanish**: 1 entry
    - **Japanese**: 11 entries
    - **Malayalam**: 3 entries
    - **Chinese**: 2 entries

### Summary
- **Highest Rated Movies**: Movies with a rating of 5 stars are "Inside Man," "Fidaa," "Manmadhudu 2," "Hey Sinamika," and "Meiyazhagan."
- **Lowest Rated Movies**: Movies with a rating of 1 star are very few, mainly scoring low across the board.
- **Most Frequent Rating**: 3 stars for both overall and quality ratings.

This analysis captures a comprehensive view of the provided dataset, illustrating the distribution of ratings across different languages and types of media.

## Dataset Classification

The input file contains 0 numerical columns and 8 categorical columns. ### Plot Information:


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
- by: 262 missing values
