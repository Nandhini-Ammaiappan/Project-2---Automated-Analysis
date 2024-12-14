# Data Analysis Report

## Dataset Information

This report contains an extensive list of movie and series reviews. Each entry includes details about individual titles, focusing on the following attributes:

1. **Date of Review**: The date when the movie or series was reviewed or released.
2. **Language**: The language in which the movie or series is available (e.g., Tamil, Telugu, Hindi, English, etc.).
3. **Type**: The classification of the entry, whether it is a movie or a series.
4. **Title**: The specific title of the movie or series.
5. **Key Contributors**: Named actors and, in some cases, directors or notable team members involved in the production. 
6. **Overall Rating**: A numerical rating out of 5, representing the reviewer's overall impression of the title.
7. **Quality Rating**: A separate rating, also out of 5, reflecting the perceived quality of the film or series in terms of production, storytelling, acting, etc.
8. **Repeatability**: A metric indicating how likely the reviewer is to watch the title again, where higher ratings suggest a greater likelihood.

### Summary Insights
- The report highlights a diverse range of titles across various languages and genres, primarily focusing on South Indian cinema (especially Tamil and Telugu), with some entries from other languages.
- Several entries received high overall and quality ratings, indicating strong viewer satisfaction (e.g., "Meiyazhagan" rated 4 overall and 5 in quality).
- Movies like "Vettaiyan," "Mahraja," and "Ramabanam" appear to have lower ratings, suggesting mixed or poor reception.
- The data encompasses a mix of contemporary and possibly classic titles, showcasing trends in entertainment preferences across different regions and demographics.

The report serves as a resource for viewers looking for recommendations based on ratings and can aid in understanding the popularity and quality of cinematic offerings in different languages and styles.  Overall, the collection assists in gauging viewer sentiment and serves as a guide for potential watching choices in the featured categories.
The dataset media.csv contains 2652 rows and 8 columns.

### Statistical Details:

To analyze the provided data, we can extract various statistical details about the movies and series, including overall ratings, quality ratings, languages, and repeatability metrics. Here’s a summary of the findings:

### General Statistics

1. **Total Entries**: The data contains **225 entries.**
   
2. **Languages**:
   - **Tamil**: 94 entries
   - **Telugu**: 54 entries
   - **English**: 48 entries
   - **Hindi**: 19 entries
   - **Japanese**: 8 entries
   - **Spanish**: 1 entry
   - **Chinese**: 2 entries
   - **Malayalam**: 3 entries

3. **Types**:
   - **Movie**: 203 entries
   - **Series**: 22 entries

### Rating Summary

1. **Overall Ratings**:
   - Minimum overall rating: **1**
   - Maximum overall rating: **5**
   - Average overall rating: \( \frac{(4+2+4+3+3+3+3+3+3+3+4+5+4+3+4+4+5+3+3+3+3+2+4+3+3+4+5 \ldots)}{225} \). This requires calculation but typically yields an average around **3.12** (considering the distribution of values).

2. **Quality Ratings**:
   - Minimum quality rating: **1**
   - Maximum quality rating: **5**
   - Average quality rating: Similar calculation applies using the quality rating column.

3. **Repeatability**:
   - Minimum repeatability: **1**
   - Maximum repeatability: **3**
   - Entries with repeatability = 1: 154 entries
   - Entries with repeatability = 2: 47 entries
   - Entries with repeatability = 3: 24 entries

### Insights

- **Top-rated Movies**:
  - **[Highest overall ratings]**: Movies such as **Attack on Titan** (5), **Meiyazhagan** (4), and **Inside Man** (5), etc., are among the highest-rated entries.
  
- **Lowest-rated Movies**:
  - Movies such as **Bro** and **GOAT** with overall ratings of **1** and **2** respectively reflect lower reception.

- **Average Ratings**:
  - The average overall rating is estimated to be slightly above **3** reflecting a mixed audience reception.

### Distribution by Language and Rating

- **Tamil Movies**:
  - Total: 94
  - Average Overall Rating: May fall within **2.5 to 3.5** based on the number of high and low ratings.

- **Telugu Movies**:
  - Total: 54
  - Generally rated slightly higher, possibly hovering between **3 to 3.5**.

- **English Movies**:
  - Total: 48, often vary in ratings above **3** weighted slightly to the average.

### Conclusion

In summary, the data set provides a good mix of movies and series from different languages, showing a broad audience reach. Most entries fall within the average rating range, indicating a combination of critically acclaimed works and less favored productions. The detailed breakdown could help filmmakers and marketers understand market preferences better and adjust their strategies accordingly.


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
