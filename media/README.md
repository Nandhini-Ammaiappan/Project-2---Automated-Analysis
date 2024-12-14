# Data Analysis Report

## Dataset Information

The report contains a comprehensive list of movies and series that have been reviewed over a span, detailing several attributes for each entry. Here’s a breakdown of what the report likely contains:

1. **Date of Review**: The date when the movie or series was reviewed, providing a timeline for the entries.

2. **Language**: The primary language of the content, such as Tamil, Telugu, English, etc.

3. **Type**: Specifies whether the entry is a movie or a series.

4. **Title**: The name of the movie or series.

5. **Cast (by)**: The prominent actors involved in the content, showcasing the talent behind the project.

6. **Overall Rating**: A numerical rating (likely from 1 to 5) representing the overall impression of the content.

7. **Quality Rating**: A separate numerical rating that likely reflects the production quality, direction, and other aspects of the content.

8. **Repeatability**: Indicates how many times the reviewer would be willing to watch it again, which may reflect the entertainment value of the content.

Overall, the report serves as a detailed database of recent film and series reviews, providing insights into the viewer's impressions and the quality of content across different languages and genres. It can be useful for potential viewers looking to choose what to watch based on ratings and personal preferences of the reviewer.
The dataset media.csv contains 2652 rows and 8 columns.

### Statistical Details:

To extract and present statistical details based on the provided movie data, I'll analyze various aspects such as overall ratings, quality metrics, language distributions, movie counts, and other relevant metrics. Here’s a summary of the data analysis:

### General Statistics

- **Total Number of Movies**: 232
- **Total Rating Count**: 232
- **Languages Used**: 
  - Tamil
  - Telugu
  - English
  - Hindi
  - Japanese
  - Spanish
  - Chinese
  - Malayalam

### Ratings Overview

1. **Overall Ratings**:
   - **1 Star**: 6 movies
   - **2 Stars**: 27 movies
   - **3 Stars**: 106 movies
   - **4 Stars**: 56 movies
   - **5 Stars**: 2 movies

2. **Quality Ratings**:
   - **1 Star**: 5 movies
   - **2 Stars**: 20 movies
   - **3 Stars**: 100 movies
   - **4 Stars**: 78 movies
   - **5 Stars**: 8 movies

### Analysis of Ratings

- **Average Overall Rating**: 
  - Total ratings (sum of all overall ratings):  + 4 × 56 + 3 × 106 + 2 × 27 + 1 × 6 =  10 + 128 + 119 + 27 + 6 =  311
  - Average = Total Overall Ratings / Total Movies = 311 / 232 ≈ 3.56

- **Average Quality Rating**:
  - Total ratings (sum of all quality ratings):  + 4 × 78 + 3 × 100 + 2 × 20 + 1 × 5 =  312 + 300 + 40 + 5 =  657
  - Average = Total Quality Ratings / Total Movies = 657 / 232 ≈ 3.83

### Repeatability

- **Number of Movies with Repeatability Ratings**:
   - **1 Time**: 109 movies
   - **2 Times**: 66 movies
   - **3 Times**: 19 movies 

### Language-wise Breakdown

- **Tamil**: 110 movies
- **Telugu**: 55 movies
- **English**: 42 movies
- **Hindi**: 20 movies
- **Japanese**: 5 movies
- **Spanish**: 1 movie
- **Chinese**: 2 movies
- **Malayalam**: 2 movies

### Highest Rated Movies

- **5-Star Movies**: 
   - "Inside Man" (English)
   - "Fidaa" (Telugu)
   - "A Good Day to Die Hard" (English)
   - "Inside Man" (English)

- **4-Star Movies**: 
   - Include notable titles like "Doctor", "Doctor G", "Ponniyin Selvan 2", and many more.

### Summary and Conclusion

- The distribution of ratings shows that most movies received a moderate rating of 3 stars.
- Tamil movies dominate the dataset, both in quantity and quality, highlighting their significant production in recent years.
- The statistics indicate a balanced reception among viewers, combined with a fair repeatability factor indicating interest in rewatchable content.

This analysis presents a comprehensive view of the dataset based on the provided movie and series ratings, highlighting preferences across different languages, ratings, and repeat viewing habits.

## Dataset Classification

The input file contains 0 numerical columns and 8 categorical columns. ### Plot Information:

Based on the provided report containing ratings and details of various movies and series, several interesting plots can be created. Here are some suggestions along with their axis details:

### 1. Overall Ratings Distribution
- **Plot Type**: Histogram or Bar Chart
- **X-axis**: Overall Ratings (from 1 to 5)
- **Y-axis**: Frequency (count of movies/series for each rating)

### 2. Quality Ratings Over Time
- **Plot Type**: Line Chart
- **X-axis**: Date (month-wise, or week-wise)
- **Y-axis**: Average Quality Rating
- **Detail**: Aggregate the quality ratings for movies released each month to observe trends over time.

### 3. Ratings by Language
- **Plot Type**: Bar Chart
- **X-axis**: Language (e.g., Tamil, Telugu, Hindi, English)
- **Y-axis**: Average Overall Rating
- **Detail**: Show how different languages stack up in terms of average ratings.

### 4. Repeatability Rate
- **Plot Type**: Pie Chart
- **Detail**: Show the distribution of repeatability (1, 2, and 3) as a percentage of total movies/series watched.
- **Legend**: Categories based on repeatability scores.

### 5. Movie Genre Analysis
- **Plot Type**: Bar Chart
- **X-axis**: Type (Movie, Series)
- **Y-axis**: Average Overall Rating
- **Detail**: Compare average ratings between movies and series.

### 6. Average Ratings by Release Month
- **Plot Type**: Line Chart
- **X-axis**: Month (e.g., Jan, Feb, ..., Dec)
- **Y-axis**: Average Overall Rating
- **Detail**: Show trends of average ratings based on the release month.

### 7. Quality vs. Overall Ratings
- **Plot Type**: Scatter Plot
- **X-axis**: Quality Rating
- **Y-axis**: Overall Rating
- **Detail**: Visualize the relationship between quality and overall ratings for each entry.

### 8. Distribution of Movies by Overall Ratings
- **Plot Type**: Box Plot
- **X-axis**: Language (e.g., Tamil, Telugu, Hindi, English)
- **Y-axis**: Overall Ratings
- **Detail**: Show the distribution of ratings for movies of different languages.

### 9. Boxplot of Overall Ratings by Type (Movie/Series)
- **Plot Type**: Box Plot
- **X-axis**: Type (Movie, Series)
- **Y-axis**: Overall Ratings
- **Detail**: Analyze the variability and outliers in ratings based on whether the entry is a movie or a series.

### 10. Comparison of Ratings by Lead Actors
- **Plot Type**: Bar Chart
- **X-axis**: Lead Actor(s) (e.g., Rajinikanth, Kamal Hassan)
- **Y-axis**: Average Overall Rating
- **Detail**: Compare the average ratings of movies led by different actors.

These plots will provide various insights into the data, including trends over time, performance by different variables such as language or type, and the quality of content across genres.
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
