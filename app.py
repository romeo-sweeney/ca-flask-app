from flask import Flask, render_template, request
import pandas as pd
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_data():
    try:
        # Get the uploaded file
        file = request.files['file_input']
        house_number = request.form['house_number']

        # Preprocess the CSV content to remove leading whitespaces on the first line
        file_content = file.read().decode('utf-8').lstrip()

        # Create a new StringIO object with the modified content
        modified_file = StringIO(file_content)

        # Process the data using pandas (replace this with your processing logic)
        df = pd.read_csv(modified_file)

        # Case-insensitive matching for 'House' column
        df['House'] = df['House'].str.strip()  # Remove leading/trailing whitespaces
        filtered_data = df[df['House'].str.lower() == house_number.lower()]

        # Get the list of matching email addresses separated by semicolons
        email_list = ';'.join(filtered_data['Email'].dropna())

        return render_template('result.html', result=email_list)

    except Exception as e:
        return render_template('error.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
