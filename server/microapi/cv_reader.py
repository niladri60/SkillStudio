from flask import Flask, request, jsonify
import os
import tempfile
import mysql.connector
from dotenv import load_dotenv
from parser import parse_cv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Connect to MySQL database
def connect_to_database():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE")
        )
    except mysql.connector.Error as error:
        print(f"Error: {error}")
        return None

# Create necessary table if it does not exist
def create_user_cvs_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_cvs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            user_name VARCHAR(255),
            file_path VARCHAR(255),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

# Helper function to save the uploaded file temporarily
def save_temp_file(uploaded_file):
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, uploaded_file.filename)
    uploaded_file.save(file_path)
    return file_path

@app.route('/upload_cv', methods=['POST'])
def upload_cv():
    if 'user_id' not in request.form:
        return jsonify({"error": "No user ID provided"}), 400
    if 'cv' not in request.files:
        return jsonify({"error": "No CV file provided"}), 400

    user_id = request.form['user_id']
    cv_file = request.files['cv']
    file_type = cv_file.filename.split('.')[-1].lower()

    if file_type not in ['pdf', 'docx']:
        return jsonify({"error": "Unsupported file type"}), 400

    file_path = save_temp_file(cv_file)
    
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        create_user_cvs_table(cursor)

        # Retrieve the user's name from the users table
        cursor.execute("SELECT username FROM users WHERE id=%s", (user_id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "User not found"}), 404
        
        user_name = user[0]

        # Save the CV details
        cursor.execute("""
            INSERT INTO user_cvs (user_id, user_name, file_path) 
            VALUES (%s, %s, %s)
        """, (user_id, user_name, file_path))
        
        conn.commit()

        # Parse the CV
        parsed_data = parse_cv(file_path, file_type)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify(parsed_data)

if __name__ == '__main__':
    app.run(debug=True)
