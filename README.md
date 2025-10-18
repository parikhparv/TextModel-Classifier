# TextModel Classifier

A Python project that models and compares text using linguistic features such as word frequency, stems, and sentence structure.  
It can classify an unknown text by comparing it to two known sources based on their linguistic patterns.

---

## 🧠 Description

This project implements a `TextModel` class that analyzes a body of text by extracting and quantifying key linguistic features.  
The model can then compare different texts and determine which source a new “mystery” text is most similar to.

This project demonstrates fundamental concepts in natural language processing (NLP), including:
- Text cleaning and tokenization  
- Feature extraction (word lengths, stems, punctuation, etc.)  
- Log similarity scoring  
- Text classification between two source models  

---

## ⚙️ Features

- **Clean and preprocess text:** Removes punctuation and converts words to lowercase.  
- **Feature extraction:** Builds dictionaries for:
  - Word frequencies  
  - Word lengths  
  - Stems (using a basic stemming function)  
  - Sentence lengths  
  - Punctuation frequency  
- **Similarity scoring:** Uses log probability to measure how similar one text is to another.  
- **Classification:** Compares a mystery text against two sources and predicts which one it most likely came from.  
- **File I/O:** Can save and load text models to and from files.  

