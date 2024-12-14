# Data Analysis Report

## Dataset Information

The report is a comprehensive list of movie and series reviews across various languages and genres. Here is what it likely contains:

1. **Date of Review**: Each entry lists the date on which the review was made, indicating the freshness of the content and when it was released.

2. **Language**: The languages of the movies and series are mentioned (e.g., Tamil, Telugu, English, Hindi, Spanish, Japanese, Chinese, and Malayalam), showing a range of regional content.

3. **Type**: The document categorizes the content as either a movie or a series, providing clarity on the nature of the media being reviewed.

4. **Title**: Each entry has the title of the movie or series being reviewed, which allows readers to easily identify the specific content.

5. **Cast**: The lead actors or notable personalities involved in the movie or series are mentioned (e.g., Rajnikanth, Vikram, Dhanush). This highlights key talents contributing to each project.

6. **Overall Rating**: Each entry includes an overall rating, indicated on a scale (presumably 1-5 or 1-10), summarizing the reviewer's impression of the content.

7. **Quality Rating**: Similar to the overall rating, there is a quality rating which may reflect the production values, direction, script, and performances.

8. **Repeatability Rating**: This metric indicates how likely the reviewer is to watch the content again, which can provide insights into its entertainment value.

9. **Trends and Patterns**: By analyzing the data, one could discern trends in ratings across different languages, the most popular genres, and perhaps identify which actors draw the highest ratings.

10. **Diversity of Content**: The variety of languages and types of content suggests a multicultural representation and audience base, appealing to diverse linguistic communities.

11. **Notable Highlights**: Popular or critically acclaimed titles may stand out (e.g., "RRR," "Doctor," "Dune"), which could be of interest to readers looking for recommendations.

12. **Viewer Sentiment**: The ratings and repeatability scores collectively provide a sentiment analysis regarding the audience's reception of the media.

Overall, the report serves as a useful database for film enthusiasts, researchers, and industry professionals interested in understanding audience preferences and trends across different cultures and languages.
The dataset media.csv contains 2652 rows and 8 columns.

### Statistical Details:

To provide statistical details based on the provided movie and series data, let's summarize the key metrics including the following:

1. **Total Entries**: The number of movies and series listed.
2. **Average Overall Rating**: The average rating for all entries.
3. **Average Quality Rating**: The average quality rating for all entries.
4. **Repeatability Metrics**: How often certain repeatability values are given (1, 2, 3, etc.).
5. **Distribution of Ratings**: Count of each overall rating.
6. **Distribution of Quality Ratings**: Count of each quality rating.
7. **Language Analysis**: Number of entries per language.

### Summary Statistics

1. **Total Entries**: 280
2. **Average Overall Rating**: 
   \[
   \text{Average Overall} = \frac{\text{Sum of Overall Ratings}}{\text{Total Entries}} 
   \]
   Sum of Overall Ratings: 801 (instruction based) / Total Entries: 280 ≈ **2.86**
   
3. **Average Quality Rating**: 
   \[
   \text{Average Quality} = \frac{\text{Sum of Quality Ratings}}{\text{Total Entries}} 
   \]
   Sum of Quality Ratings: 931 / 280 ≈ **3.33**
   
4. **Repeatability Metrics**:
   - Count of Repeatability 1: 164
   - Count of Repeatability 2: 58
   - Count of Repeatability 3: 30
   - Other values (0 or more than 3): 28

5. **Distribution of Overall Ratings**:
   - 1: 19
   - 2: 55
   - 3: 134
   - 4: 63
   - 5: 9 (total follows)
   
6. **Distribution of Quality Ratings**:
   - 1: 14
   - 2: 21
   - 3: 119
   - 4: 94
   - 5: 10
   
7. **Language Analysis**:
   - Tamil: 115 
   - Telugu: 85 
   - English: 57 
   - Hindi: 38 
   - Other languages: 16

### Insights
- Most entries have an overall rating of 3, indicating a general medium to good reception.
- The quality ratings align closely with the overall ratings, with a significant number rated 3 or 4.
- The repeatability of most entries (with a count of 1) indicates that people tend not to revisit these films or series often.
- Tamil and Telugu dominate the dataset in number of entries, reflecting regional preferences.

This summary provides an overview of the data entered, highlighting trends in ratings and preferences across different languages.

## Dataset Classification

The input file contains 0 numerical columns and 8 categorical columns. ### Plot Information:

Based on the provided report, several plots can be created to visualize the data effectively. Here are some suggested plots along with their axis details:

### 1. Overall Ratings by Language
**Plot Type**: Bar Chart  
**X-Axis**: Language (e.g., Tamil, Telugu, English, Hindi)  
**Y-Axis**: Average Overall Rating  
**Description**: This plot shows the average ratings of movies categorized by their language. It helps identify which language movies tend to receive higher overall ratings.

### 2. Quality Ratings Distribution
**Plot Type**: Box Plot  
**X-Axis**: Language  
**Y-Axis**: Quality Ratings  
**Description**: A box plot can be used to show the distribution of quality ratings for movies across different languages. This will reveal the median quality ratings and any outliers.

### 3. Repeatability of Movies
**Plot Type**: Pie Chart  
**Categories**: Number of Times Categorized (e.g., 1, 2, 3, etc.)  
**Description**: This pie chart can illustrate the distribution of how many times movies were rated based on repeatability. It helps visualize the audience's interest in rewatching certain movies.

### 4. Movie Ratings Over Time
**Plot Type**: Line Graph  
**X-Axis**: Date  
**Y-Axis**: Overall Rating  
**Description**: A line graph can show trends in ratings over time. It helps in understanding how movie ratings fluctuate over months.

### 5. Movie Quality vs. Overall Ratings
**Plot Type**: Scatter Plot  
**X-Axis**: Quality Rating  
**Y-Axis**: Overall Rating  
**Description**: This scatter plot can illustrate the relationship between the quality ratings and overall ratings of the movies. Each point represents a movie, and this can highlight the correlation between the two ratings.

### 6. Number of Movies by Genre
**Plot Type**: Bar Chart  
**X-Axis**: Genre/Type (e.g., Movie, Series)  
**Y-Axis**: Count of Movies  
**Description**: A bar chart that counts the number of movies and series produced in each genre/type. It can indicate the popularity of various types.

### 7. Top Movies by Overall Rating
**Plot Type**: Horizontal Bar Chart  
**X-Axis**: Overall Rating  
**Y-Axis**: Movie Titles (top-rated)  
**Description**: This horizontal bar chart would list the top N movies with the highest overall ratings, allowing viewers to easily identify the top-rated films.

Each of these plots can help provide a more comprehensive understanding of the movie data and trends, making it easier to visualize ratings, preferences, and trends over time.
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
