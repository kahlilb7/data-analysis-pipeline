# Name: Kahlil Batieste
# Date: 03/18/2026
# Description: This program analyzes a movie dataset and generates summary statistics and insights.
# Dataset: movies.csv

# constant storing the dataset filename
DATASET = "movies.csv"

# -------------------------------
# Step 2: Define load_data function
# -------------------------------
def load_data(filepath):
    """
    Loads data from a CSV file and returns a list of dictionaries.
    """
    data = []