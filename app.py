from flask import Flask, request, jsonify
import pandas as pd
from bs4 import BeautifulSoup

app = Flask(__name)

def convert_html_to_excel(html_content):
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the table
    table = soup.find('table')

    if table:
        # Convert the table to a DataFrame using pandas
        df = pd.read_html(str(table))[0]

        # Save the DataFrame to an Excel file
        excel_file = 'table_to_excel.xlsx'
        df.to_excel(excel_file, index=False)
        return excel_file
    else:
        return None

@app.route('/html_to_excel', methods=['POST'])
def html_to_excel():
    # Get HTML content from the POST request
    html_content = request.data.decode('utf-8')

    excel_file = convert_html_to_excel(html_content)

    if excel_file:
        return excel_file, 200
    else:
        return 'No table found in HTML content', 400

if __name__ == '__main__':
    app.run(debug=True)
