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
    # reads through each record in the dataset and converts the specified column's value to a float,
    # appending it to the values list
    low = min(values)
    high = max(values)
    avg = round(sum(values) / len(values), 2)

    return low, high, avg


# ---------------------------------------
# Define summarize function
# ---------------------------------------
def summarize(data):
    """Returns summary statistics for the dataset."""
    
    total_records = len(data)

    genres = []
    ratings = []

    for record in data:
        genres.append(record["genre"])
        ratings.append(float(record["rating"]))

    unique = []

    for genre in genres:
        if genre not in unique:
            unique.append(genre)

    unique_genres = len(unique)
    average_rating = round(sum(ratings) / len(ratings), 2)

    return {
        "total_records": total_records,
        "unique_genres": unique_genres,
        "average_rating": average_rating}


# ---------------------------------------
# Define display_summary function
# ---------------------------------------
def display_summary(data):
    """Displays the summary statistics."""
    
    summary = summarize(data)

    print("Total Records:", summary["total_records"])
    print("Unique Genres:", summary["unique_genres"])
    print("Average Rating:", summary["average_rating"])


# ------------------------------------------------------------------------
# Define generate_insights function and return insights about the dataset.
# ------------------------------------------------------------------------
def generate_insights(data):
    """Generates insights about the dataset."""
    
    insights = []

    rating_stats = get_category_stats(data, "rating")
    value_stats = get_category_stats(data, "value")
    summary = summarize(data)

    insights.append("The average rating is " + str(summary["average_rating"]) + ".")
    insights.append("The highest rating in the dataset is " + str(rating_stats[1]) + ".")
    insights.append("The highest value in the dataset is " + str(value_stats[1]) + ".")
    
    return insights


# ---------------------------------------
# Define export_report function
# ---------------------------------------
def export_report(data, output_filepath, top_n=5):
    """Exports the top N records to a file."""
    
    summary = summarize(data)
    insights = generate_insights(data)

    sorted_data = data[:]

    for i in range(len(sorted_data)):
        for j in range(i + 1, len(sorted_data)):
            if float(sorted_data[j]["rating"]) > float(sorted_data[i]["rating"]):
                temp = sorted_data[i]
                sorted_data[i] = sorted_data[j]
                sorted_data[j] = temp

    top_records = sorted_data[:top_n]

    with open(output_filepath, "w") as file:
        file.write("Dataset Summary\n")
        file.write("Total Records: " + str(summary["total_records"]) + "\n")
        file.write("Unique Genres: " + str(summary["unique_genres"]) + "\n")
        file.write("Average Rating: " + str(summary["average_rating"]) + "\n\n")

        file.write("Insights\n")
        for insight in insights:
            file.write("- " + insight + "\n")

        file.write("\nTop Records by Rating\n")
        for record in top_records:
            line = (
                record["title"]
                + " | Year: " + record["year"]
                + " | Genre: " + record["genre"]
                + " | Rating: " + record["rating"]
                + " | Value: " + record["value"]
            )
            file.write(line + "\n")