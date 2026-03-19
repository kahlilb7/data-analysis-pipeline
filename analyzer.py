# Name: Kahlil Batieste
# Date: 03/18/2026
# Description: This program analyzes a movie dataset and generates summary statistics and insights.
# Dataset: movies.csv

#----------------------------------------------
# Step 1: constant storing the dataset filename
#----------------------------------------------
DATASET = "movies.csv"

# ---------------------------------
# Step 2: Define load_data function
# ---------------------------------
def load_data(filepath):
    """Loads data from a CSV file and returns a list of dictionaries."""
    
    data = []


# ---------------------------------------
# Step 3: Open the file using "with" loop
# ---------------------------------------
    with open(filepath, "r") as file:
    
    
        # ---------------------------------------------------------
        # Step 4: Read lines from the file and store them in a list
        # ---------------------------------------------------------
        lines = file.readlines()


        # -----------------------------------------------------------------
        # Step 5: Skip the header row only produce lines below the header.
        # -----------------------------------------------------------------
        lines = lines[1:]


        # -----------------------------------------------------------------------
        # Step 6: Loop through each line and process into correct data structure.
        # -----------------------------------------------------------------------
        for line in lines:  


        # -----------------------------------------------------------
        # Step 7: Split line into parts and store in a formated list.
        # -----------------------------------------------------------
            parts = line.strip().split(",") 

        
        # -------------------------------------------------------------
        # Step 8: Assign values to variables and store in a dictionary.
        # -------------------------------------------------------------
            title = parts[0]
            year = parts[1]
            genre = parts[2]
            rating = parts[3]
            value = parts[4]


        # ---------------------------------------------
        # Step 9: Create dictionary for 
        # row and append to data list then return data.
        # ---------------------------------------------
            record = {
                "title": title,
                "year": year,
                "genre": genre,
                "rating": rating,
                "value": value}
            data.append(record)
        return data


#----------------------------------------
# Define filter_data function 
# ---------------------------------------
def filter_data(data, column, value):
    """Filters the dataset based on a column and value."""
    filtered = []
# Loop through each record in the dataset and check if the 
# specified column matches the value. If it does, add the record to the filtered list.
    for record in data:
        if record[column] == value:
            filtered.append(record)
    return filtered


# -------------------------------------------------------
# Define get_category_stats function and return 
# the minimum, maximum, and average for a numeric column.
# -------------------------------------------------------
def get_category_stats(data, column):
    """Returns the minimum, maximum, and average for a numeric column."""
    values = []

    for record in data:
        values.append(float(record[column]))

    low = min(values)
    high = max(values)
    avg = round(sum(values) / len(values), 2)

    return low, high, avg