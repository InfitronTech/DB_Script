import psycopg2
import json

# Function to query the database and fetch data
def fetch_data(names):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname='mayan',
        user='mayan',
        password='mayandbpass',
        host='192.168.100.36'
    )
    cursor = conn.cursor()

    # Initialize result list
    result = []

    # Query the database for each name
    for name in names:
        # Execute the query
        cursor.execute("SELECT id, label FROM public.cabinets_cabinet WHERE label = %s", (name,))
        row = cursor.fetchone()

        # If a record is found, store the id and label in the result list
        if row:
            result.append({'id': row[0], 'label': row[1]})
        else:
            print(f"No record found for {name}")

    # Close the database connection
    conn.close()

    return result

# List of names to query the database
# Read names from CSV file
# names_to_query = []
# with open('names.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         names_to_query.extend(row)

# Read names from TXT file
names_to_query = []
with open('names.txt', 'r') as txtfile:
    for line in txtfile:
        names_to_query.append(line.strip())

# Fetch data from the database
data = fetch_data(names_to_query)

# Convert the data to the desired format
formatted_data = [
    { 'id': entry['id'], 'label': entry['label'] } for entry in data
]

# Export the data as a JSON file
with open('data.json', 'w') as f:
    json.dump(formatted_data, f, indent=4)

print("Data exported successfully.")
