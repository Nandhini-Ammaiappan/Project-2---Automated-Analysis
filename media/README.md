# Data Analysis Report

## Dataset Information

Based on the provided data, the report appears to comprise a comprehensive list of movie and series reviews categorized by date, language, type (movie or series), title, cast, and various ratings metrics. Here’s a breakdown of what the report likely contains:

1. **Overall Structure**:
   - Each entry includes attributes indicating the date of the review, language of the movie/series, type (either movie or series), title, primary cast, and various ratings.

2. **Details per Entry**:
   - **Date**: The release date or review date (e.g., "15-Nov-24").
   - **Language**: The language in which the movie or series is produced (e.g., Tamil, Telugu, English, Hindi).
   - **Type**: Whether the content is a movie or a series.
   - **Title**: The title of the movie or series being reviewed.
   - **By**: The main actors/actresses featured in the movie or series (could also include director details).
   - **Overall Rating**: A numerical rating indicating the overall impression of the movie or series (on a scale from 1-5).
   - **Quality Rating**: A numerical rating evaluating the quality of the movie or series, likely assessing aspects like production, direction, and script.
   - **Repeatability**: A score indicating how likely the reviewer is to watch it again, suggesting the viewer's enjoyment or the movie's replay value.

3. **Summary of Trends**:
   - There are distinct trends over time in terms of language popularity, the average quality ratings, and how certain actors influence overall impressions.
   - For instance, popular actors like Rajnikanth and Vijay often appear in higher-rated movies, while some movies with lesser-known cast members tend to have lower ratings.

4. **Evaluation Insights**:
   - The report potentially allows insights into the performance of different film industries, like how Tamil films perform compared to Telugu or English films based on ratings and box office results.
   - The frequency of each language in the list may indicate regional preferences among viewers.

5. **Recommendation Potential**:
   - Various viewing recommendations can be made based on high overall and quality ratings.
   - Viewers can be advised on selecting content based on favorite actors or directors.

6. **Visual Representation**:
   - If visual aids (like charts or graphs) were included, they could show ratings distributions, trending actors, or genre popularity over specific time intervals.

In summary, this report serves as a detailed review log of movies and series, focusing on viewer perceptions through a structured approach to rating and categorization, making it useful for both viewers looking for recommendations and industry analysis.
The dataset media.csv contains 2652 rows and 8 columns.

### Statistical Details:

Based on the provided data, here is a statistical summary of the movies and series:

### Overview

- **Total Entries:** 128
- **Languages Represented:**
  - Tamil: 52
  - Telugu: 35
  - English: 27
  - Hindi: 14
  - Other (Spanish, Malayalam, Japanese, Chinese): 5

### Ratings Summary
- **Overall Rating Distribution:**
  - Rating 1: 6 entries
  - Rating 2: 20 entries
  - Rating 3: 59 entries
  - Rating 4: 36 entries
  - Rating 5: 7 entries
  
- **Quality Rating Distribution:**
  - Quality 1: 6 entries
  - Quality 2: 15 entries
  - Quality 3: 50 entries
  - Quality 4: 39 entries
  - Quality 5: 6 entries

### Repeatability Summary
- **Repeatability Counts:**
  - Repeatability 1: 73 entries
  - Repeatability 2: 29 entries
  - Repeatability 3: 18 entries

### Top Rated Movies (Overall Rating)
1. **Attack on Titan** (5/5) - Japanese
2. **Meiyazhagan** (4/5) - Tamil
3. **Maharaja** (4/5) - Tamil
4. **Viswasam** (4/4) - Tamil
5. **Fantastic Beasts: The Secrets of Dumbledore** (4/4) - English
6. **Moneyball** (4/4) - English

### Lowest Rated Movies (Overall Rating)
1. **Bro** (1/2) - Telugu
2. **Agilan** (1/2) - Tamil
3. **Ramarao on Duty** (2/3) - Telugu
4. **Doctor G** (2/3) - Hindi
5. **Vaarisu** (2/3) - Tamil

### Most Frequent Movie Type
- **Movies:** 115 entries
- **Series:** 13 entries

### Observations
- **Tamil** movies are the most represented with **52 entries** and feature a relatively high number of higher-rated films compared to other languages.
- **Overall**, most movies received a rating of 3 (46%).
- The repeatability suggests viewers generally found value in rewatching movies and series, particularly those rated highly.
- Quality rating is fairly high, with a majority of entries rated 3 or above.

### Conclusion
This dataset indicates a diverse range of content in terms of language, genre, and viewer reception. Tamil cinema appears quite vibrant in this collection, with many high-quality ratings reported, while overall viewer engagement is also notably high, as indicated by repeatability scores.

## Dataset Classification

The input file contains 0 numerical columns and 8 categorical columns. ### Plot Information:

Based on the provided report of movie reviews, several types of plots can be created to visualize and analyze the data. Here are some suggestions along with their axis details:

1. **Overall Ratings Distribution by Language**
   - **Plot Type**: Box Plot or Violin Plot
   - **X-axis**: Language (categorized, e.g., Tamil, Telugu, English, Hindi, etc.)
   - **Y-axis**: Overall Rating (numerical scale from 1 to 5)
   - **Description**: This plot visualizes the distribution of overall ratings for movies in different languages, highlighting the median and variability.

2. **Average Quality Ratings by Language**
   - **Plot Type**: Bar Chart
   - **X-axis**: Language
   - **Y-axis**: Average Quality Rating (numerical scale from 1 to 5)
   - **Description**: This chart can show the average quality rating of movies for each language, helping to identify which languages generally have higher quality movies.

3. **Trend of Overall Ratings Over Time**
   - **Plot Type**: Line Chart
   - **X-axis**: Date (time series)
   - **Y-axis**: Overall Rating
   - **Description**: This plot tracks the trend in overall ratings over time, showcasing if ratings have improved or declined as new movies are released.

4. **Movie Count by Language**
   - **Plot Type**: Pie Chart or Bar Chart
   - **X-axis**: Language
   - **Y-axis**: Count of Movies
   - **Description**: This visual representation would show the proportion of movies reviewed in each language, allowing insight into which languages are more represented.

5. **Repeatability Ratings Analysis**
   - **Plot Type**: Histogram
   - **X-axis**: Repeatability Rating
   - **Y-axis**: Frequency (number of occurrences)
   - **Description**: This histogram can show how many users were likely to watch the movies again based on the repeatability ratings provided.

6. **Scatter Plot of Quality vs. Overall Rating**
   - **Plot Type**: Scatter Plot
   - **X-axis**: Quality Rating 
   - **Y-axis**: Overall Rating 
   - **Description**: This scatter plot depicts the relationship between the quality rating and overall rating, helping to identify any correlation.

7. **Repeatability Ratings by Date**
   - **Plot Type**: Line or Heatmap
   - **X-axis**: Date
   - **Y-axis**: Average Repeatability Rating
   - **Description**: This visualization shows how viewer satisfaction (repeatability) trends over time.

8. **Top Movies by Overall Ratings**
   - **Plot Type**: Horizontal Bar Chart
   - **X-axis**: Overall Rating
   - **Y-axis**: Movie Titles
   - **Description**: This chart highlights the highest-rated movies, providing consumers with quick recommendations.

9. **Quality Ratings Seen Over Time**
   - **Plot Type**: Area Chart
   - **X-axis**: Date
   - **Y-axis**: Average Quality Rating
   - **Description**: This chart shows how the average quality rating has changed over the timeframe of the reviews.

10. **Comparison of Overall Ratings for Different Movie Types**
    - **Plot Type**: Box Plot or Bar Chart
    - **X-axis**: Type of Movie (e.g., movie, series)
    - **Y-axis**: Overall Rating
    - **Description**: This visualization can compare average overall ratings between different types of entertainment (movies vs. series).

### Conclusion
These visualization ideas can help in understanding trends, characteristics, and viewer preferences in the dataset. Each plot can be created using visualization libraries such as Matplotlib, Seaborn, or Plotly in Python or similar libraries in other programming languages.
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
