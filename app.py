from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    html_input = request.form['html_input']
    # Convert HTML to Excel using Pandas
    # Replace this with your own conversion logic
    df = pd.read_html(html_input)
    df.to_excel('output.xlsx', index=False)
    # Then, send the Excel file to the user
    return send_file('output.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
