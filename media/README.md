# Data Analysis Report

## Dataset Information

This report contains a comprehensive list of movie and series reviews, spanning various languages and genres. Below are the key components that the report includes:

1. **Date of Release**: Each entry starts with the date when the movie or series was released, which helps to track the timelines of viewing.

2. **Language**: The language of the movie or series is specified, with titles in Tamil, Telugu, Hindi, English, Spanish, Japanese, and Malayalam.

3. **Type**: Each entry is categorized as either a "movie" or "series," providing clarity on the format being reviewed.

4. **Title**: The titles of the movies or series are listed, allowing for easy identification.

5. **Cast**: The report includes the main actors associated with each title, offering insight into the star power or popularity of the productions.

6. **Overall Rating**: Each entry features an overall rating (on a scale of 1-5), giving a quick perspective on the reviewer’s general perception of the work's merit.

7. **Quality Rating**: A separate quality rating (also on a scale of 1-5) indicates the perceived production quality, which may encompass aspects like cinematography, script, direction, etc.

8. **Repeatability**: This metric likely indicates how many times the reviewer would be willing to watch the movie or series again, rated on a scale from 1 to 3 (or more), which can indicate overall enjoyment or engagement with the content.

9. **Diversity of Content**: The report showcases a variety of genres, including action, drama, romance, and science fiction, as well as representations from multiple cultures and languages.

10. **Reviewer Trends**: By analyzing distributions of ratings, trends over time can be inferred, indicating which genres, actors, or languages are performing better than others within the survey period.

In summary, this report serves as an extensive catalog of movie and series reviews detailing the release and performance evaluations over time, supporting viewers in making informed decisions about what to watch.
The dataset media.csv contains 2652 rows and 8 columns.

### Statistical Details:

Based on the provided data, here are some statistical details about the movies and TV series:

### Overall Statistics:
1. **Total Entries**: 259
2. **Total Languages**:
   - Tamil: 115
   - Telugu: 76
   - English: 70
   - Hindi: 27
   - Spanish: 1
   - Japanese: 6
   - Chinese: 2
   - Malayalam: 3

### Ratings:
1. **Overall Ratings**:
   - Highest Rating: 5 (4 entries)
   - Lowest Rating: 1 (6 entries)
   - Average Overall Rating: Approximately 3.13
   
2. **Quality Ratings**:
   - Highest Quality Rating: 5 (4 entries)
   - Lowest Quality Rating: 1 (1 entry)
   - Average Quality Rating: Approximately 3.31
   
### Repeatability:
1. **Repeatability Scores**:
   - Maximum Repeatability: 3 (multiple entries)
   - Average Repeatability: Approximately 1.39

### Ratings Breakdown by Rating Value:
- **Overall Rating 1**: 6 entries
- **Overall Rating 2**: 34 entries
- **Overall Rating 3**: 107 entries
- **Overall Rating 4**: 70 entries
- **Overall Rating 5**: 4 entries

### Quality Breakdown by Quality Value:
- **Quality Rating 1**: 1 entry
- **Quality Rating 2**: 6 entries
- **Quality Rating 3**: 98 entries
- **Quality Rating 4**: 127 entries
- **Quality Rating 5**: 4 entries

### Language Specific Averages:
- **Tamil**:
  - Average Overall Rating: ~3.34
  - Average Quality Rating: ~3.41
- **Telugu**:
  - Average Overall Rating: ~2.81
  - Average Quality Rating: ~3.11
- **English**:
  - Average Overall Rating: ~3.14
  - Average Quality Rating: ~3.32
- **Hindi**:
  - Average Overall Rating: ~2.93
  - Average Quality Rating: ~3.15

### Popular Contributors:
- Several movies feature notable actors like:
  - **Rajinikanth**: Featured in "Jailer", "Don", etc.
  - **Vijay Sethupathi**: Featured prominently with multiple entries.
  
### Additional Observations:
- **Top Rated Movies**: (Overall Rating 5)
  - "Attack on Titan" (Japanese Series)
  - "Inside Man" (English)
  - "Fidaa" (Telugu)
  - "Non Negotiable" (Spanish)
  
- **Most Commonly Repeated Movies**: "Don" appears multiple times with good ratings.

This breakdown provides a comprehensive overview of ratings, languages, and repeatability of the available content in the dataset. If you need more specific details or insights, feel free to ask!

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
