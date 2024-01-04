from livescore_api import livescore
from tabulate import tabulate
from jinja2 import Environment, FileSystemLoader

api = livescore()

# Fetching the first 10 matches (you can adjust the number as needed)
matches = api.matches()[:23]

# Prepare data for the template
table_headers = matches[13].keys() if matches else []
table_data = [match.values() for match in matches]

# Prepare Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render the template
output = template.render(table_headers=table_headers, table_data=table_data)

# Save the HTML content to a file
with open('matches_table.html', 'w') as file:
    file.write(output)

print("HTML file generated: matches_table.html")
