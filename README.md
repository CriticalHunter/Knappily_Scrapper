# Knappily_Scrapper
Scrape articles from the news/article content site [knappily.com](https://knappily.com) 

Additional metadata includes links to article, date and category. 

      
## :heavy_check_mark: Features
This project does the following tasks

1. There are 14 categories in the website. And query is made for each category.
2. For each category the Selenium driver hits the load more page ~50 times  (limit by website)
      1. Process exists and continues for next category is no more page are there.
3. Output is a CSV file.

        

## Working Guide

1. Run the program scrape_knappily.py

2. Chromedriver.exe should be downloaded and kept in the path
      1. Or the path can be modified, if it is at some other location


### Known Issues
1. Try running for 3-4 categories at once. Running loop for all 14 categories will take time and may fail due to temporary network issue.

## :hearts: Contributing
There are several ways to help. 

1. **Spread the word:** More users means more possible people testing and contributing to the app which in turn means better stability and possibly more and better features. You can [![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FCriticalHunter%2FKnappily_Scrapper)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FCriticalHunter%2FKnappily_Scrapper.git) or share it on [LinkedIn](http://www.linkedin.com/shareArticle?mini=true&url=https://github.com/CriticalHunter/Knappily_Scrapper.git). Every little bit helps ! 

2. **[Make a feature or improvement request](https://github.com/CriticalHunter/Knappily_Scrapper/issues/new)**: Something can be be done better? Something essential missing? Let us know! 
