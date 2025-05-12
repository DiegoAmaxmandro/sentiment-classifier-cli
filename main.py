# Imports
import pandas as pd
import sys
from utils import clean_text
from transformers import pipeline
import os

# Loading data
def load_reviews(file_path):
    df = pd.read_csv(file_path)
    print("\n First 5 reviews loaded:\n")
    print(df.head())
    return df



# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py path_to_file.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    df = load_reviews(input_file)

    # Cleaning text
    os.makedirs("outputs", exist_ok=True)
    df['cleaned'] = df['review'].apply(clean_text)
    print('\n Cleaned reviews preview: \n')
    print(df[['review', 'cleaned']].head())

    # Classifying text
    print('\n Loading sentiment classifier \n')
    classifier = pipeline('sentiment-analysis')

    print('Classifying sentiment... \n')
    df['sentiment'] = df['cleaned'].apply(lambda text: classifier(text)[0]['label'])

    print('\n Classification complete: \n')
    print(df[['review', 'cleaned', 'sentiment']])

    # Export to JSON
    output_path = 'outputs/classified_reviews.json'
    df.to_json(output_path, orient='records', indent=2)
    print(f"\n Exported results to {output_path}")

