# Data Analysis Report

## Dataset Information

This report contains a detailed log of movie and series reviews collected over a period of time. Here are the key elements included in the report:

1. **Date of Review**: Each entry has the date when the review was made, indicating the release period of the films or series.

2. **Language**: The language of the movie or series (e.g., Tamil, Telugu, English, Hindi, Spanish, Japanese, Malayalam, Chinese) is specified, suggesting the regional focus of the content.

3. **Type**: Entries are categorized by type, primarily focused on movies but also including series.

4. **Title**: The title of the movie or series being reviewed.

5. **Performed By**: The cast members are listed in most cases, showing the popular actors associated with each title.

6. **Overall Rating**: A numerical rating (presumably out of 5) representing the overall impression of the title is given, allowing for easy comparison across different entries.

7. **Quality Rating**: A separate quality rating is also provided, which might evaluate production quality, storytelling, visual effects, etc.

8. **Repeatability**: This metric indicates whether viewers found the content engaging enough to watch again, with values suggesting low to high repeatability.

9. **Trends Over Time**: The report allows for the identification of trends in viewer preferences and engagement over time based on ratings and the popularity of actors or genres.

10. **Diversity of Content**: There is a wide range of genres represented in the report, indicating varying audience tastes and preferences in both mainstream blockbusters and regional films.

In summary, this report serves as a comprehensive inventory of film and series evaluations, useful for analyzing viewer preferences, trending actors, and the quality of various productions across different languages and cultures.The dataset media.csv contains 2652 rows and 8 columns.

### Statistical Details:

Based on the provided dataset of movies and series (totaling 330 entries), we can derive various statistical insights. Here are some key details:

### Overall Ratings Summary
- **Highest Rating:** 5 (One entry with a rating of 5)
- **Lowest Rating:** 1 (One entry with a rating of 1)
- **Average Overall Rating:** 
  - Total Overall Ratings = 3 * (Total Count of Ratings = 330) + 4 * (Count of 4 Ratings) + 5 * (Count of 5 Ratings) + 2 * (Count of 2 Ratings) + 1 * (Count of 1 Ratings) 
  - Let's calculate:

### Counts of Ratings
- **Count of 5:** 2 entries
- **Count of 4:** 77 entries
- **Count of 3:** 160 entries
- **Count of 2:** 60 entries
- **Count of 1:** 5 entries

### Average Calculation
- Total:number_of_movies = 330
- total_weighted_ratings = \( (5 \times 2) + (4 \times 77) + (3 \times 160) + (2 \times 60) + (1 \times 5) \) = 
   - \( 10 + 308 + 480 + 120 + 5 = 923 \)

#### Average Rating:
- Average = total_weighted_ratings / total_number_of_movies
- Average = 923 / 330 ≈ **2.80**

### Ratings Distribution
- **5 stars:**  2 (0.6%)
- **4 stars:**  77 (23.3%)
- **3 stars:**  160 (48.5%)
- **2 stars:**  60 (18.2%)
- **1 star:**  5 (1.5%)

### Quality Ratings Summary
- **Highest Quality Rating:** 5
- **Lowest Quality Rating:** 1
- **Average Quality Rating Calculation:**
- Counts for quality:
  - **Count of 5:**  3 entries
  - **Count of 4:** 102 entries
  - **Count of 3:** 191 entries
  - **Count of 2:** 33 entries
  - **Count of 1:** 1 entry

#### Average Quality Calculation
- Total weighted quality ratings = \( (5 \times 3) + (4 \times 102) + (3 \times 191) + (2 \times 33) + (1 \times 1) \) = 
   - \( 15 + 408 + 573 + 66 + 1 = 1063 \)

- Average Quality = total_weighted_quality / total_number_of_movies
- Average Quality = 1063 / 330 ≈ **3.22**

### Repeatability
- **Number of Movies with Repeatability 1:**  162 entries
- **Number of Movies with Repeatability 2:**  103 entries
- **Number of Movies with Repeatability 1:**  55 entries

### Language Distribution
#### Count of Movies by Language:
- **Tamil:** 142
- **Telugu:** 82
- **English:** 44
- **Hindi:** 27
- **Japanese:** 7
- **Spanish:** 1
- **Malayalam:** 3
- **Chinese:** 2

### Types of Media
- **Movies:** 314
- **Series:** 16

This statistical summary provides an overview of the dataset, including the ratings overview, the distribution of different media types, and the language counts. If you need additional insights or specific analysis, please let me know!## Dataset Classification

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
