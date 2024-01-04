# LiveScore Matches Table

This project fetches live sports match data using the LiveScore API, displays the information in a table, and generates an HTML file for easy viewing in a browser.

## Dependencies

Make sure you have the required Python libraries installed. You can install them using:

```bash
pip install livescore_api tabulate Jinja2
```

## Usage
Run the Python script to fetch live match data and generate the HTML file:

```bash
python3 live_score.py
```

Open the generated HTML file (matches_table.html) in a web browser to view the live matches table.

## Project Structure

- **livescore.py**: The Python script to fetch live match data and generate the HTML file.
- **template.html**: The Jinja2 template file for the HTML output.
- **matches_table.html**: The generated HTML file containing the live matches table.

## Acknowledgments

- **LiveScore API**: [Link to LiveScore API](https://www.livescore.com/)
- **Tabulate**: [Link to Tabulate](https://pypi.org/project/tabulate/)
- **Jinja2**: [Link to Jinja2](https://palletsprojects.com/p/jinja/)
