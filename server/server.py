from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)

# Configure Database (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soil_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class SoilData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    npk = db.Column(db.Float)
    ph = db.Column(db.Float)
    moisture = db.Column(db.Float)

# Create the database if it doesn't exist
if not os.path.exists('soil_data.db'):
    db.create_all()

# API route to receive sensor data
@app.route('/api', methods=['POST'])
def api():
    try:
        data = request.get_json()
        npk = data['npk']
        ph = data['ph']
        moisture = data['moisture']
        
        # Save data to the database
        new_data = SoilData(npk=npk, ph=ph, moisture=moisture)
        db.session.add(new_data)
        db.session.commit()

        return jsonify({"message": "Data saved successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route for the dashboard
@app.route('/')
def dashboard():
    # Retrieve the latest data from the database
    data = SoilData.query.all()
    # Pass data to the HTML template
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
