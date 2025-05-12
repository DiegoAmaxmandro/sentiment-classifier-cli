# Imports
import re

# Function to clean the text
def clean_text(text):
    text = text.lower() # Lowecase
    text = re.sub(r'[^a-z0-9\s]', '', text) #Removing punctuations, numbers and special characters
    text = re.sub(r'\s+', ' ', text).strip() # Removing extra white space
    return text