from flask import Flask
import json  
import psycopg2

app = Flask(__name__)

@app.route('/')
def home_page():
    message = 'You are on the / page. Navigate to a different path like api/questions'
    return message

@app.route('/api/questions')
def return_questions():
    #establishing the connection to the db
    conn = psycopg2.connect(
        database="mydb", user='myuser', password='mypassword', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions") #SQL query to get all the questions
    data = cursor.fetchall() #stores the questions in a variable called data
    jsonified = json.dumps(data)
    return jsonified

    # getting the json from a file rather than the backend
    # with open('questions.json') as f: 
    #     data = json.load(f)
    #     return data
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

