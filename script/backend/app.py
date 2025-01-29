from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app) 

# User ID to Name Mapping
user_names = {
    4: "Anna",
    1948: "Juan",
    2: "Miguel"
}

def get_db_connection():
    return mysql.connector.connect(
        host='destination_db',  # Use the Docker service name
        user='root',
        password='root',
        database='destination_db'
    )

@app.route('/')
def home():
    return "Welcome to the Backend API!"

@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Reports by Users (user_id)
    cursor.execute("""
        SELECT user_id, COUNT(*) AS total_reports
        FROM reports
        GROUP BY user_id
    """)
    users_data = cursor.fetchall()

    # Map user_id to user names
    for user in users_data:
        user["user_name"] = user_names.get(user["user_id"], f"User {user['user_id']}")

    # Extensionist Approval (approval column: 1 = Approved, NULL = Not Approved)
    cursor.execute("""
        SELECT 
            COUNT(CASE WHEN extensionist_approval = 1 THEN 1 END) AS approved,
            COUNT(CASE WHEN extensionist_approval IS NULL THEN 1 END) AS not_approved
        FROM reports
    """)
    extensionist_data = cursor.fetchone()

    # Chairperson Approval (approval column: 1 = Approved, NULL = Not Approved)
    cursor.execute("""
        SELECT 
            COUNT(CASE WHEN chairperson_approval = 1 THEN 1 END) AS approved,
            COUNT(CASE WHEN chairperson_approval IS NULL THEN 1 END) AS not_approved
        FROM reports
    """)
    chairperson_data = cursor.fetchone()

    # Dean Approval (approval column: 1 or 2 = Approved, NULL or 0 = Not Approved)
    cursor.execute("""
        SELECT 
            COUNT(CASE WHEN dean_approval IN (1, 2) THEN 1 END) AS approved,
            COUNT(CASE WHEN dean_approval IS NULL OR dean_approval = 0 THEN 1 END) AS not_approved
        FROM reports
    """)
    dean_data = cursor.fetchone()

    connection.close()

    # Prepare the response data for frontend consumption
    analytics = {
        "users": [{"user_name": user["user_name"], "total_reports": user["total_reports"]} for user in users_data],
        "extensionist_approval": {
            "approved": extensionist_data["approved"],
            "not_approved": extensionist_data["not_approved"]
        },
        "chairperson_approval": {
            "approved": chairperson_data["approved"],
            "not_approved": chairperson_data["not_approved"]
        },
        "dean_approval": {
            "approved": dean_data["approved"],
            "not_approved": dean_data["not_approved"]
        }
    }
    
    return jsonify(analytics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
