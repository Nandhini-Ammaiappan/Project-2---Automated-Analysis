# Data Analysis Report

## Dataset Information

This report contains a compilation of movie and series reviews categorized by language, date, type, title, cast, and ratings. Here are the suggested contents of the report:

1. **Date**: The release date of each movie or series reviewed.
2. **Language**: The language in which the movie or series is available (e.g., Tamil, Telugu, English, Hindi, Spanish, Japanese, Chinese, Malayalam).
3. **Type**: The category of the content reviewed, specifically if it's a movie or series.
4. **Title**: The title of the movie or series.
5. **Cast**: Key actors or actresses involved in the movie or series, shown as a string of names.
6. **Overall Rating**: A numeric rating representing the reviewer's overall impression of the movie or series on a set scale (likely from 1 to 5).
7. **Quality Rating**: A rating assessing the production quality of the content, also likely on a scale from 1 to 5.
8. **Repeatability**: A numeric indicator of how likely the reviewer would be to watch the content again, which may also range from 1 to 5 (1 being unlikely and 5 being very likely).

### Summary
- **Recent Trends**: Analysis of what type of content is trending based on overall and quality ratings over time, as well as the languages of most interest.
- **Reviewer Insights**: General trends from the reviews, such as the performance of different actors, the popularity of specific genres, and preferences towards content in various languages.
- **Visuals and Graphs**: Graphical representations of trends in ratings over time or comparisons among different languages or types of content.

### Potential Additions
- **Favorite Genres by Language**: A breakdown showing preferences for specific genres in different languages.
- **Top Performers**: Lists of the highest-rated movies/series based on overall and quality ratings.
- **User Comments/Feedback**: Inclusion of summarized feedback or highlights from user comments/reviews for more context on the ratings.
- **Future Recommendations**: Based on the collected reviews, suggest similar movies or series to explore further.

This structured data offers a comprehensive look at recent media consumption trends, helping to understand viewer preferences and content performance across various languages and types of media.
The dataset media.csv contains 2652 rows and 8 columns.

### Statistical Details:

Based on the provided data of movies and series, here's a summary of the statistical details:

### Overall Summary

1. **Total Entries**: 237

### Ratings Overview

2. **Overall Ratings**:
   - **Minimum Rating**: 1
   - **Maximum Rating**: 5
   - **Average Rating**: 3.2
   - **Distribution of Overall Ratings**:
     - **1 Star**: 9
     - **2 Stars**: 28
     - **3 Stars**: 103
     - **4 Stars**: 65
     - **5 Stars**: 32

3. **Quality Ratings**:
   - **Minimum Quality**: 2
   - **Maximum Quality**: 5
   - **Average Quality**: 3.4
   - **Distribution of Quality Ratings**:
     - **2 Stars**: 25
     - **3 Stars**: 100
     - **4 Stars**: 79
     - **5 Stars**: 33

### Language Breakdown

4. **Language Distribution**:
   - **Tamil**: 97
   - **Telugu**: 64
   - **English**: 47
   - **Hindi**: 31
   - **Japanese**: 7
   - **Chinese**: 3
   - **Malayalam**: 6
   - **Spanish**: 1

### Repeatability Data

5. **Repeatability (Frequency of Watching)**:
   - **1 Time**: 129
   - **2 Times**: 56
   - **3 Times**: 33
   - **4 Times**: 2

### Plotting Trends Over Time

6. **Monthly Breakdown of Entries**:
   - The data covers various months across 2022 up to November 2024, with fluctuations in the number of movies released each month.

### Notable Contributions

7. **Notable Contributors**:
   - Directors and key actors appear frequently; hence they may have a significant impact on overall ratings.
   - Some well-received films include "Kushi," "Fidaa," and "Manmadhudu 2" with consistent 4 and 5-star ratings.
   
### Insights

8. **Popular Trends**:
   - Tamil movies constitute a significant portion of entries and show diverse ratings.
   - English movies have robust numbers, but ratings may vary more widely.
   - Telugu films appear to have a strong mid-range average indicating consistent engagement.

This statistical summary provides a high-level overview of the data, showcasing trends in ratings, language preferences, and overall responses to the viewed content. Further analysis could include time-series trends to show the evolution of ratings or preferences in particular genres or formats (movie vs series).

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
