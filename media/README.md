# Description of the file


MEDIA.CSV is used as input for the analysis. This file contains 2652 rows and 8 columns.
The file contains data with the following columns: 'date', 'language', 'type', 'title', 'by', 'overall', 'quality', 'repeatability'. The 'date' column likely holds date information regarding when entries were made. The 'language' column likely indicates the language of the content. The 'type' column could specify the category or genre of the entry. The 'title' column likely contains the name or title of the content. The 'by' column may indicate the author or creator. The 'overall' column seems to be a numerical representation, possibly a rating or score. The 'quality' column likely assesses the quality of the content, possibly also a numeric value, while 'repeatability' might indicate how often a certain observation can be repeated, possibly on a categorical or numerical scale.
Data in the file can contain ['categorical', 'numerical', 'time-series']

### Statistical Details:


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
## Graphical Representation of data

![Bar_plot.png](Bar_plot.png)
