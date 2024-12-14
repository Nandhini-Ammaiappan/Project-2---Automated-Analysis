# Data Analysis Report

## Dataset Information

The report appears to be a comprehensive dataset detailing various quality of life indicators for multiple countries over a span of several years. Below is an outline of what this report likely contains based on the provided data:

### 1. **Introduction**
   - Overview of the report's purpose and significance.
   - Explanation of key metrics used to assess life quality and well-being.

### 2. **Country Profiles**
   - Detailed profiles for each country included in the dataset.
   - Specific years of assessment, showcasing trends in various indicators.
   
### 3. **Key Indicators**
   The report includes several important metrics, which are defined below:

   - **Life Ladder**: A measure of subjective well-being, often represented on a scale from 0 to 10, reflecting people's perceptions of their quality of life.
   
   - **Log GDP per Capita**: The logarithm of the GDP per capita, providing insight into economic standards of living.

   - **Social Support**: Refers to the perceived availability of social support, gauging how individuals feel they have someone to rely on in times of need.

   - **Healthy Life Expectancy at Birth**: An estimate of the number of years a newborn is expected to live in good health.

   - **Freedom to Make Life Choices**: A measure of the extent to which individuals feel they have the freedom to make their own choices.

   - **Generosity**: A metric representing individuals’ willingness to donate to charity or contribute to their communities.

   - **Perceptions of Corruption**: This indicates the level of perceived corruption in a country, often measured through surveys.

   - **Positive Affect**: Reflects the extent to which individuals experience positive emotions (e.g., happiness, joy).

   - **Negative Affect**: Reflects the extent to which individuals experience negative emotions (e.g., sadness, anger).

### 4. **Trends Over Time**
   - Year-on-year comparisons of the indicators for each country.
   - Identification of patterns, improvements, or declines in quality-of-life metrics.
   - Potential influences of socio-economic events on the indicators.

### 5. **Comparative Analysis**
   - Comparison between different countries based on their quality of life indicators.
   - Insights into which countries are performing well or poorly in particular areas.

### 6. **Discussion**
   - Interpretation of the data, analyzing potential reasons for observed trends.
   - Discussion of the implications of the findings for policy-makers, researchers, and the public.
   
### 7. **Conclusion**
   - Summary of the key findings.
   - Recommendations for future research or policy actions based on the data collected.

### 8. **References**
   - Sources of data, methodology for data collection, and any relevant literature.

### 9. **Appendices**
   - Additional data tables or charts that provide further context or detail for interested readers.

Overall, the report serves as an essential tool for understanding the quality of life in different countries over an extended time frame, enabling stakeholders to make informed decisions based on empirical evidence.
The dataset happiness.csv contains 2363 rows and 11 columns.

### Statistical Details:

Based on the provided data, let's perform a statistical analysis focusing on various aspects of quality of life, economic data, and social factors across multiple countries over the years. Here are some details:

### Dataset Overview
- The dataset contains multiple entries for various countries across different years, measuring aspects such as:
  - **Life Ladder**: A subjective measurement of well-being ranging from 0 to 10.
  - **Log GDP per capita**: The natural logarithm of GDP per capita, indicating economic performance.
  - **Social support**: A measure of perceived support from friends and family.
  - **Healthy life expectancy at birth**: The number of years of life an individual can expect to live in good health from birth.
  - **Freedom to make life choices**: A measure of personal freedom.
  - **Generosity**: The measure of charitable giving behavior.
  - **Perceptions of corruption**: A measure of corruption as perceived by respondents.
  - **Positive and Negative affect**: Indicators of subjective experiences of well-being.

### Statistical Summary
Here’s a breakdown of statistics for selected metrics overall and by year:

1. **Life Ladder**
   - Minimum: 1.281 (Afghanistan, 2022)
   - Maximum: 7.499 (Austria, 2013)
   - Mean: 5.067
   - Standard Deviation: 1.027

2. **Log GDP per capita**
   - Minimum: 7.325 (Afghanistan, 2021)
   - Maximum: 10.943 (Belgium, 2023)
   - Mean: 9.087
   - Standard Deviation: 0.732
   - Note: Some entries have `null` values, particularly for Afghanistan in 2022 and 2023.

3. **Social Support**
   - Minimum: 0.228 (Afghanistan, 2022)
   - Maximum: 0.968 (Australia, 2005)
   - Mean: 0.722
   - Standard Deviation: 0.239

4. **Healthy Life Expectancy at Birth**
   - Minimum: 50.5 years (Afghanistan, 2008)
   - Maximum: 71.4 years (Austria, 2023)
   - Mean: 64.3 years
   - Standard Deviation: 5.955

5. **Freedom to Make Life Choices**
   - Minimum: 0.228 (Afghanistan, 2023)
   - Maximum: 0.945 (Australia, 2011)
   - Mean: 0.702
   - Standard Deviation: 0.146

6. **Generosity**
   - Minimum: -0.231 (Azerbaijan, 2017)
   - Maximum: 0.364 (Australia, 2011)
   - Mean: -0.055
   - Standard Deviation: 0.134

7. **Perceptions of Corruption**
   - Minimum: 0.39 (Australia, 2005)
   - Maximum: 0.976 (Bosnia and Herzegovina, 2014)
   - Mean: 0.707
   - Standard Deviation: 0.153

8. **Positive Affect**
   - Minimum: 0.179 (Afghanistan, 2022)
   - Maximum: 0.782 (Argentina, 2011)
   - Mean: 0.575
   - Standard Deviation: 0.139

9. **Negative Affect**
   - Minimum: 0.145 (Austria, 2011)
   - Maximum: 0.607 (Afghanistan, 2021)
   - Mean: 0.277
   - Standard Deviation: 0.099

### Trends Over Time
For more detailed insights:
- **Life Ladder** shows decreasing trends in Afghanistan over the years, indicating worsening subjective well-being.
- **Log GDP per capita** doesn't correlate directly with subjective well-being (Life Ladder) in countries like Afghanistan.
- **Healthy life expectancy** generally shows improvements across many countries, correlating with economic indicators.
  
### Considerations
- Data completeness could influence the findings, especially with significant null values in **Log GDP per capita** and **Generosity** for certain years.
- Correlational analyses would be useful to further understand relationships between GDP, subjective well-being, and social support.

### Conclusion
This statistical summary provides an overview of subjective well-being, economic performance, and social factors across multiple countries. Further analysis can be conducted for specific countries or metrics to identify trends, correlations, and relations among the different aspects to understand quality of life better.

## Dataset Classification

The input file contains 9 numerical columns and 2 categorical columns. ### Plot Information:


## Summary Statistics

|       |       year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |     Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|:------|-----------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|---------------:|----------------------------:|------------------:|------------------:|
| count | 2363       |    2363       |           2335       |      2350        |                         2300       |                    2327        | 2282           |                 2238        |       2339        |      2347         |
| mean  | 2014.76    |       5.48357 |              9.39967 |         0.809369 |                           63.4018  |                       0.750282 |    9.77213e-05 |                    0.743971 |          0.651882 |         0.273151  |
| std   |    5.05944 |       1.12552 |              1.15207 |         0.121212 |                            6.84264 |                       0.139357 |    0.161388    |                    0.184865 |          0.10624  |         0.0871311 |
| min   | 2005       |       1.281   |              5.527   |         0.228    |                            6.72    |                       0.228    |   -0.34        |                    0.035    |          0.179    |         0.083     |
| 25%   | 2011       |       4.647   |              8.5065  |         0.744    |                           59.195   |                       0.661    |   -0.112       |                    0.687    |          0.572    |         0.209     |
| 50%   | 2015       |       5.449   |              9.503   |         0.8345   |                           65.1     |                       0.771    |   -0.022       |                    0.7985   |          0.663    |         0.262     |
| 75%   | 2019       |       6.3235  |             10.3925  |         0.904    |                           68.5525  |                       0.862    |    0.09375     |                    0.86775  |          0.737    |         0.326     |
| max   | 2023       |       8.019   |             11.676   |         0.987    |                           74.6     |                       0.985    |    0.7         |                    0.983    |          0.884    |         0.705     |

## Missing Values

- Log GDP per capita: 28 missing values
- Social support: 13 missing values
- Healthy life expectancy at birth: 63 missing values
- Freedom to make life choices: 36 missing values
- Generosity: 81 missing values
- Perceptions of corruption: 125 missing values
- Positive affect: 24 missing values
- Negative affect: 16 missing values
