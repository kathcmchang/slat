import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import FreqDist
import pandas as pd

nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')

class NLTKProcessor:
    def __init__(self, keywords):
        self.keywords = keywords
        self.sia = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))

    def process(self, text):
        tokenized_text = nltk.word_tokenize(text)
        filtered_text = [word for word in tokenized_text if word.casefold() not in self.stop_words]

        keyword_frequencies = FreqDist(word for word in filtered_text if word in self.keywords)

        sentiment_scores = self.sia.polarity_scores(text)

        return keyword_frequencies, sentiment_scores

def calculate_score(row):
    return row['keyword_count'] + (row['sentiment_positive'] - row['sentiment_negative']) * row['keyword_count']

keywords = ['sustainability', 'green', 'eco-friendly', 'renewable', 'recycle', 'carbon-neutral', 'net-zero', 'climate change', 'energy efficiency', 'waste management', 'conservation', 'biodiversity', 'emission', 'clean', 'organic', 'natural resources', 'pollution', 'environmental', 'sustainable development', 'greenhouse']

processor = NLTKProcessor(keywords)

# Read the CSV file into a DataFrame
df = pd.read_csv("scraped_data.csv")

# Add columns for keyword count and sentiment scores
df['keyword_count'] = 0
df['sentiment_positive'] = 0.0
df['sentiment_neutral'] = 0.0
df['sentiment_negative'] = 0.0
df['sentiment_compound'] = 0.0

# Process the content of each row
for index, row in df.iterrows():
    keyword_frequencies, sentiment_scores = processor.process(row['content'])
    df.loc[index, 'keyword_count'] = sum(keyword_frequencies.values())
    df.loc[index, 'sentiment_positive'] = sentiment_scores.get('pos', 0.0)
    df.loc[index, 'sentiment_neutral'] = sentiment_scores.get('neu', 0.0)
    df.loc[index, 'sentiment_negative'] = sentiment_scores.get('neg', 0.0)
    df.loc[index, 'sentiment_compound'] = sentiment_scores.get('compound', 0.0)


# Calculate scores
df['score'] = df.apply(calculate_score, axis=1)

# Categorize into tiers based on quantiles of the scores
df['tier'] = pd.qcut(df['score'], q=3, labels=['low', 'medium', 'high'])

# Drop the 'content' column
df = df.drop(columns=['content'])

# Save to CSV
df.to_csv('sustainability_scores.csv', index=False)
