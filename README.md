# Sustainability Language Analysis Tool (SLAT)
# Overview
The Sustainability Language Analysis Tool (SLAT) is a project aimed at assessing the commitment of SMEs to sustainability and Net Zero goals. It does this by scraping text data from public communications of SMEs, such as their websites and social media profiles, and then using natural language processing (NLP) techniques to analyze the data.

# Key Features

* Web Scraping: SLAT uses Scrapy, a powerful open-source web crawling framework, to gather the required text data.

* Text Analysis: The tool uses various NLP techniques for analyzing the text data. This includes tokenization, lemmatization, keyword counting and sentiment analysis to count the frequency of sustainability-related keywords and understand the sentiment behind the language used when discussing sustainability. The keyword frequency and sentiment scores are then used to calculate a sustainability score for each company.

* Rating Algorithm: Based on the results of the language analysis, SLAT includes an algorithm that rates the companies' commitment to sustainability. Companies are categorized into three tiers of sustainability commitment (low, medium, high) based on the quantiles of their sustainability scores.

# Tech Stack
* Scrapy
* Natural Language Toolkit (NLTK)
* BeautifulSoup
* pandas



Please note that this tool is intended for educational and research purposes. Always respect the terms of use of any website you scrape.
