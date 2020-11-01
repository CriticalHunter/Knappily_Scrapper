# Knappily_Scrapper
Scrape articles from the news/article content site knappily.com . 

Additional metadata includes links to article, date and category. 
Output is a CSV file.

1. There are 14 categories in the website. And query is made for each category.
2. For each category the Selenium driver hits the load more page ~50 times  (limit by website)
      1. Process exists and continues for next category is no more page are there.
### Known Issues
1. Try running for 3-4 categories at once. Running loop for all 14 categories will take time and may fail due to temporary network issue.
