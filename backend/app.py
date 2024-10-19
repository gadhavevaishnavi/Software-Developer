from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('registration.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/registrations', methods=['GET'])
def get_registrations():
    conn = get_db_connection()
    registrations = conn.execute('SELECT * FROM Registration').fetchall()
    conn.close()
    return jsonify([dict(registration) for registration in registrations])

@app.route('/registrations', methods=['POST'])
def create_registration():
    new_registration = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber, Address)
        VALUES (?, ?, ?, ?, ?)
    ''', (new_registration['name'], new_registration['email'], new_registration['date_of_birth'], new_registration.get('phone_number'), new_registration.get('address')))
    conn.commit()
    conn.close()
    return jsonify(new_registration), 201

if __name__ == '__main__':
    app.run(debug=True)
