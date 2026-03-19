# Name: Kahlil Batieste
# Date: 03/18/2026
# Description: This program analyzes a movie dataset and generates summary statistics and insights.
# Dataset: movies.csv

# constant storing the dataset filename
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


