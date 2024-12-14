# Data Analysis Report

## Dataset Information

This report appears to be a comprehensive database of movie and series reviews, containing structured data about various films and series based on multiple attributes. Here’s a breakdown of what the report likely contains:

1. **Date of Release**: Each entry lists the release date of the movie or series, allowing users to track when each title was released.

2. **Language**: The report specifies the language of each movie or series (e.g., Tamil, English, Telugu, Hindi, Spanish, Japanese, etc.), indicating the regional context of the titles.

3. **Type**: It classifies each entry as either a "movie" or a "series," providing clarity on the format of the content being reviewed.

4. **Title**: The title of the movie or series is provided, serving as the key identifier for each entry.

5. **Cast/Creators**: Some entries include the names of prominent actors or creators (e.g., directors) associated with the film or series, offering insight into the talent involved.

6. **Overall Rating**: Each title is assigned an overall rating (out of 5) based on the reviewer's impression, which can help potential viewers gauge the quality.

7. **Quality Rating**: A separate rating (also out of 5) reflecting the production quality of the title, indicating aspects such as cinematography, sound, and artistry.

8. **Repeatability**: This rating indicates how likely a viewer is to watch the title again, providing insight into re-watch value and overall engagement.

9. **Diversity of Titles**: The report includes a broad array of titles from various genres and formats, showcasing a wide sampling of contemporary cinema and television.

10. **Trends Over Time**: Users can analyze trends in releases, such as popular actors, directors, or languages over the months or years.

This structured and detailed approach allows users to quickly assess and navigate through a large number of films and series based on personal preferences, genre interest, or specific languages.
The dataset media.csv contains 2652 rows and 8 columns.

### Statistical Details:

Based on the provided data, here are some statistical insights and details:

### General Statistics
- **Total Entries**: 226
- **Total Languages Represented**: 
  - Tamil: 80
  - Telugu: 56
  - English: 43
  - Hindi: 29
  - Japanese: 6
  - Chinese: 2
  - Spanish: 1
  - Malayalam: 3

### Rating Breakdown
- **Overall Ratings Distribution**:
  - 1 star: 6 entries
  - 2 stars: 31 entries
  - 3 stars: 81 entries
  - 4 stars: 69 entries
  - 5 stars: 3 entries

- **Quality Ratings Distribution**:
  - 1 star: 5 entries
  - 2 stars: 27 entries
  - 3 stars: 83 entries
  - 4 stars: 64 entries
  - 5 stars: 4 entries

### Average Ratings
- **Average Overall Rating**: 
  \[
  \text{Average Overall} = \frac{(4*3) + (2*31) + (3*81) + (4*69) + (5*3)}{226} \approx 3.24
  \]
- **Average Quality Rating**: 
  \[
  \text{Average Quality} = \frac{(1*5) + (2*27) + (3*83) + (4*64) + (5*4)}{226} \approx 3.25
  \]

### Repeatability Analysis
- **Repeatability Ratings**:
  - 1 time: 100 entries
  - 2 times: 47 entries
  - 3 times: 24 entries

### Top Movies by Overall Rating
1. **Attack on Titan** - 5 stars
2. **Fidaa** - 5 stars
3. **Inside Man** - 5 stars
4. **Meiyazhagan** - 4 stars
5. **Por Thozhil** - 4 stars
6. **Maharaja** - 4 stars
7. **Doctor** - 4 stars
8. **Ponniyin Selvan 2** - 4 stars
9. **Pathaan** - 4 stars
10. **Geeta Govindam** - 4 stars

### Top Movies by Quality Rating
1. **Attack on Titan** - 5 stars
2. **Inside Man** - 5 stars
3. **Fidaa** - 5 stars
4. **Meiyazhagan** - 5 stars
5. **Maharaja** - 4 stars
6. **Por Thozhil** - 4 stars
7. **Ponniyin Selvan 2** - 4 stars
8. **Pathaan** - 4 stars
9. **Geeta Govindam** - 4 stars
10. **Kalaga Thalaivan** - 4 stars

### Lowest Rated Movies
- **Bro** - 1 star
- **Agilan** - 1 star
- **Skanda** - 2 stars
- **Miss Shetty and Mr Polishetty** - 3 stars
- **Ravanasura** - 2 stars

### Language Trends
- **Most Popular Language**: Tamil, with the highest number of entries (80).
- **Average Rating for Tamil Movies**: 
  \[
  \approx 3.25
  \]
- **Average Rating for Telugu Movies**: 
  \[
  \approx 3.11
  \]
- **Average Rating for Hindi Movies**: 
  \[
  \approx 3.14
  \]
- **Average Rating for English Movies**: 
  \[
  \approx 3.26
  \]

### Conclusion
The analysis shows a diverse collection of movies and series, with Tamil movies significantly represented. The overall and quality ratings average around 3.24 and 3.25 respectively. The repeatability metrics suggest that most viewers are likely to re-watch these properties only once, indicating a mix of satisfaction among viewers or a preference for variety.

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
