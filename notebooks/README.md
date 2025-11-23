
# ** Minimum Essential EDA for Analyst Ratings Dataset**

This script performs the **minimum required Exploratory Data Analysis (EDA)** on the analyst ratings/news dataset as part of Task 1. The goal is to understand the structure, quality, and patterns within the news data before performing sentiment analysis or linking it to stock movements.

---

## **📌 What This Script Does**

### ✔ 1. Load & Clean the Data

* Reads the `analyst_ratings.csv` file.
* Converts the `date` column to datetime format.
* Removes rows with missing headlines or invalid dates.

---

### ✔ 2. Headline Text Analysis

* Computes headline length (number of words).
* Plots a distribution of headline lengths to understand writing patterns.

---

### ✔ 3. Publisher Analysis

* Counts articles published by each publisher.
* Shows the top 10 publishers with a bar chart.

---

### ✔ 4. Publication Date Trends

* Extracts the date-only portion of timestamps.
* Visualizes daily article counts across the dataset.
* Helps identify high-activity news days.

---

### ✔ 5. Keyword & Topic Signals

* Cleans headlines (lowercase, remove symbols).
* Extracts most common keywords.
* Plots the top 20 frequent words to show dominant topics in news coverage.

---

### ✔ 6. Hour-of-Day Analysis

* Extracts publication hour (0–23).
* Plots article frequency across hours to reveal newsroom activity patterns.

---

### ✔ 7. Publisher Domain Extraction

* Attempts to extract domains from publisher names when possible.
* Displays the most common domains.

---

### ✔ 8. Save Cleaned Output

The cleaned dataset is exported to:

```
../cleaned/cleaned_analyst_ratings2.csv
```

---

## **📦 Dependencies**

The script uses:

* pandas
* numpy
* matplotlib
* seaborn
* textblob
* collections.Counter
* statsmodels
* timedelta
* vadersentiment
* sklearn

Make sure these libraries are installed before running.

---

## **📁 Input Structure**

```
Data/
└── newsData/
    └── analyst_ratings.csv
```

---

## **🚀 Purpose**

This EDA prepares the dataset for **Task 2**, where:

* Sentiment scoring will be computed
* News will be linked to stock returns
* Statistical correlation and regression analysis will be performed

