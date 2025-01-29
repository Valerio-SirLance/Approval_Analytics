import firebase_admin
from firebase_admin import credentials, db
import mysql.connector
from mysql.connector import Error
import json

# Initialize Firebase
cred = credentials.Certificate("../eqar-remote-firebase-adminsdk-fbsvc-e9bfec6efa.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://eqar-remote-default-rtdb.firebaseio.com/'
})

# Function to extract data from Firebase
def extract_data():
    ref = db.reference('2/data')  # Path to the reports data in Firebase
    data = ref.get()  # Get all reports from Firebase Realtime Database
    return data

# Function to transform data
def transform_data(data):
    transformed_data = []
    for item in data:
        # Parse report details JSON into a dictionary
        report_details = json.loads(item['report_details']) if item['report_details'] else {}

        # Prepare the data for insertion into MySQL
        transformed_item = {
            'id': item.get('id', None),
            'user_id': item.get('user_id', None),
            'sector_id': item.get('sector_id', None),
            'college_id': item.get('college_id', None),
            'department_id': item.get('department_id', None),
            'format': item.get('format', None),
            'report_category_id': item.get('report_category_id', None),
            'report_reference_id': item.get('report_reference_id', None),
            'report_code': item.get('report_code', None),
            'report_details': json.dumps(report_details),  # Store report_details as JSON in MySQL
            'report_documents': item.get('report_documents', None),
            'report_date': item.get('report_date', None),
            'extensionist_approval': item.get('extensionist_approval', None),
            'chairperson_approval': item.get('chairperson_approval', None),
            'dean_approval': item.get('dean_approval', None),  
            'created_at': item.get('created_at', None),
            'updated_at': item.get('updated_at', None),
            'report_quarter': item.get('report_quarter', None),
            'report_year': item.get('report_year', None),
            'research_status': item.get('research_status', None),
            'extension_status': item.get('extension_status', None),
            'department_status': item.get('department_status', None),
            'college_status': item.get('college_status', None),
            'sector_status': item.get('sector_status', None),
            'ipo_status': item.get('ipo_status', None),
            'is_late': item.get('is_late', None),
            'is_returned': item.get('is_returned', None)
        }
        transformed_data.append(transformed_item)
    return transformed_data

# Function to load data into MySQL
def load_data(data):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='destination_db',
            user='root',
            password='root',
            port='3307'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            for item in data:
                cursor.execute("""
                    INSERT INTO reports (
                        id, user_id, sector_id, college_id, department_id, 
                        format, report_category_id, report_reference_id, report_code, 
                        report_details, report_documents, report_date, 
                        extensionist_approval, chairperson_approval, dean_approval, 
                        created_at, updated_at, report_quarter, report_year, 
                        research_status, extension_status, department_status, 
                        college_status, sector_status, ipo_status, 
                        is_late, is_returned
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, %s
                    )
                """, (
                    item['id'], item['user_id'], item['sector_id'], item['college_id'], 
                    item['department_id'], item['format'], item['report_category_id'], 
                    item['report_reference_id'], item['report_code'], 
                    item['report_details'], item['report_documents'], item['report_date'], 
                    item['extensionist_approval'], item['chairperson_approval'], 
                    item['dean_approval'], item['created_at'], item['updated_at'], 
                    item['report_quarter'], item['report_year'], item['research_status'], 
                    item['extension_status'], item['department_status'], item['college_status'], 
                    item['sector_status'], item['ipo_status'], 
                    item['is_late'], item['is_returned']
                ))
            
            connection.commit()
            print("Data loaded successfully.")
            
    except Error as e:
        print("Error while connecting to MySQL:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# ETL Pipeline
def run_etl():
    print("Extracting data from Firebase...")
    data = extract_data()
    if data:
        print("Transforming data...")
        transformed_data = transform_data(data)
        print("Loading data into MySQL...")
        load_data(transformed_data)
    else:
        print("No data found in Firebase.")

if __name__ == "__main__":
    run_etl()
