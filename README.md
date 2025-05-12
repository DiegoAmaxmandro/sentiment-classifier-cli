# Sentiment Classifier CLI

This is a command-line tool that processes a CSV file of text reviews, cleans the text, classifies the sentiment using a Hugging Face transformer model, and exports the results to a formatted JSON file.

Perfect for beginners learning NLP, CLI tools, and Python pipelines.

---

## Features

- Load reviews from a CSV file
- Clean and normalize review text
- Use Hugging Face transformers for sentiment classification
- Export results to JSON
- Simple CLI structure, no external config needed

---

## Project Structure

```
sentiment_classifier_cli/
├── data/                        # Input CSV files
│   └── reviews.csv              # Sample input
├── outputs/                     # Output folder (ignored by Git)
│   └── classified_reviews.json  # Generated output
├── main.py                      # Entry point CLI script
├── utils.py                     # Helper functions (e.g. clean_text)
├── requirements.txt             # Python dependencies
├── .gitignore
└── README.md
```

---

## Example Input (`data/reviews.csv`)

```csv
review
"I absolutely loved this product!"
"It was a terrible experience."
"Not bad, but I’ve had better."
"Fantastic quality, I’m impressed."
"Worst purchase I’ve made this year."
```

---

## How to Run

```bash
# Install dependencies (inside a virtual environment)
pip install -r requirements.txt

# Run the tool with your input file
python main.py data/reviews.csv
```

This will create:

```
outputs/classified_reviews.json
```

---

## Sample Output (JSON)

```json
[
  {
    "review": "I absolutely loved this product!",
    "cleaned": "i absolutely loved this product",
    "sentiment": "POSITIVE"
  },
  {
    "review": "It was a terrible experience.",
    "cleaned": "it was a terrible experience",
    "sentiment": "NEGATIVE"
  }
]
```

---

## Built With

- [Transformers](https://huggingface.co/transformers/)
- [Pandas](https://pandas.pydata.org/)
- Python 3.10+

---

## Future Improvements

- [ ] Add argparse for better CLI control
- [ ] Support batch input folders
- [ ] Add confidence scores to output
- [ ] Turn into a Python package

---

## Author

Diego Lemos — [@DiegoAmaxmandro](https://github.com/diegoamaxmandro)

---

## License

MIT License
