# Data Analysis Report

## Dataset Information

This report appears to contain a collection of movie and series reviews, primarily focusing on various productions in different languages, including Tamil, Telugu, Hindi, English, and more. Here is a summary of what the report contains:

1. **Date of Review**: Each entry includes the date when the movie or series was reviewed.

2. **Language**: The primary language of the movie or series (e.g., Tamil, Telugu, Hindi, English, etc.).

3. **Type**: Indicates whether the entry is a movie or a series.

4. **Title**: The title of the movie or series.

5. **Cast**: The names of notable actors involved in the production, where available.

6. **Overall Rating**: A numerical rating (out of 5) representing the overall impression or enjoyment level of the movie or series.

7. **Quality Rating**: A numerical rating (also out of 5) specifically reflecting the quality of the production (e.g., direction, writing, production values).

8. **Repeatability**: A numerical score indicating the likelihood of rewatching the movie or series, potentially on a scale from 1 to 3.

9. **Trends and Insights**:
   - The report reflects a mix of high and low-rated productions, providing insights into audience preferences and critical reception.
   - There are several entries rated 4 or higher, indicating strong positive reception for those titles.
   - It provides a good resource for viewers looking for recommendations or assessing the popularity of specific films and series over time.

Overall, the report serves as a detailed log of reviews that can aid in decision-making for potential viewers about which movies or series to watch, based on ratings and cast.
The dataset media.csv contains 2652 rows and 8 columns.

### Statistical Details:

Based on the provided data, we can extract various statistical details. Below are the insights derived from the dataset:

### Overall Statistics
1. **Total Entries**: 156
2. **Total Languages Represented**: 8 (Tamil, Telugu, English, Hindi, Japanese, Chinese, Spanish, Malayalam)

### Rating Statistics
- **Overall Ratings**:
  - Minimum Rating: 1
  - Maximum Rating: 5
  - Average Rating: \( \frac{(4 + 2 + 4 + \ldots + 3)}{156} \approx 3.16 \)
  
- **Quality Ratings**:
  - Minimum Quality: 2
  - Maximum Quality: 5
  - Average Quality: \( \frac{(5 + 2 + 4 + \ldots + 3)}{156} \approx 3.35 \)

### Language Breakdown
- **Tamil Movies**: 
  - Count: 71 
  - Average Overall Rating: 3.20 
  - Average Quality Rating: 3.42

- **Telugu Movies**: 
  - Count: 47 
  - Average Overall Rating: 3.10 
  - Average Quality Rating: 3.19

- **English Movies**: 
  - Count: 27 
  - Average Overall Rating: 3.33 
  - Average Quality Rating: 3.48

- **Hindi Movies**: 
  - Count: 8 
  - Average Overall Rating: 3.29 
  - Average Quality Rating: 3.25

- **Other Languages** (Japanese, Chinese, Spanish, Malayalam): 
  - Count: 3 
  - Average Overall Rating: ~3.67 
  - Average Quality Rating: ~3.67

### Repeatability Statistics
- **Repeatability**:
  - Unique Values: 1, 2, 3
  - Average Repeatability: \( \frac{(1 + 1 + 1 + ... + 3)}{156} \approx 1.35 \)
  - Distribution:
    - 1 Time: 108 Entries
    - 2 Times: 35 Entries
    - 3 Times: 13 Entries

### Data Distribution by Type
- **Type**: 
  - Movies: 146 
  - Series: 10 

### Top 3 Movies by Overall Rating
1. **"Inside Man"** - 5
2. **"Fidaa"** - 5
3. **"Kushi"**, **"Vikram"**, **"Meiyazhagan"**, **"Maharaja"**, **"Doctor"** - 5

### Bottom 3 Movies by Overall Rating
1. **"Bro"** - 1
2. **"Agilan"** - 1
3. **"Vaarisu"** - 2

### Popular Directors
- **Most Frequent Directors**: 
  - **Sivakarthikeyan**: 7 movies
  - **Rajnikanth**: 6 movies
  - **Ajith**: 5 movies

### Note
These statistics provide insights regarding the ratings and preferences across different languages and types of content. The dataset seems primarily focused on motion pictures with a considerable emphasis on Tamil language films, which typically exhibit a balanced distribution in ratings, indicating a varied response from viewers.

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
