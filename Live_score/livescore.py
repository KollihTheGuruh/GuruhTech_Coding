from livescore_api import livescore
from tabulate import tabulate

api = livescore()

# Fetching the first 10 matches (you can adjust the number as needed)
matches = api.matches()[:10]

# Print raw data in a table format
table_headers = matches[0].keys() if matches else []
table_data = [match.values() for match in matches]

if table_headers:
    print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
else:
    print("No matches found.")
