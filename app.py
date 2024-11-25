from flask import Flask, jsonify, request
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load CSV data
csv_file = 'Flight_Schedule.csv'  # Replace with your CSV file name
data = pd.read_csv(csv_file)

# Convert CSV to JSON
data_json = data.to_dict(orient='records')

# API route to get all data
@app.route('/api/data', methods=['GET'])
def get_all_data():
    return jsonify(data_json)

# API route to get data by ID
@app.route('/api/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    # Assuming the CSV has an 'id' column
    record = next((item for item in data_json if item['id'] == id), None)
    if record:
        return jsonify(record)
    else:
        return jsonify({"error": "Data not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    
