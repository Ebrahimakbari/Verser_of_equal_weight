# Quran Verse Analyzer

This is a Python project that is designed to find similar weight verses in Surah Yusuf of the Quran. The tool automatically identifies and groups verses with similar characteristics in terms of word count, vowel and consonant count, and diacritic pattern.

## Features

- Loads verses of Surah Yusuf from a text file of the Quran
- Identifies and groups verses based on word count
- Examines the Arabic diacritic pattern and vowel/consonant count of each verse
- Saves the results in an output file, separating the majority group and other groups

## Installation and Usage

1. Ensure you have the latest versions of Python and standard Python libraries installed.
2. Save the Quran text file in the same directory (with the name `quran.txt`).
3. Save the Python code in a file (e.g., `quran_verse_analyzer.py`).
4. In the terminal, run the following command:

```
python quran_verse_analyzer.py
```

This will create the output file `similar_weight_verses_yusuf.txt` in the same directory.

## Development and Improvement

This project is a prototype and can be further improved in the future. Some suggestions for development include:

- Using natural language processing libraries like NLTK to enhance text analysis
- Adding the capability to compare verses based on their meaning (using semantic analysis tools)
- Creating a graphical user interface for easier interaction with the tool
- Implementing unit tests to ensure the correctness of the code

If you have any questions or suggestions, please contact the author.
