from flask import Flask
import json  
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/')
def home_page():
    message = 'You are on the / page. Navigate to a different path like api/questions'
    return message

@app.route('/api/questions')
def return_questions():
    #establishing the connection to the db. Note that the host is 'db' because that's the name of the service in the docker-compose file
    conn = psycopg2.connect(
        database="mydb", user='myuser', password='mypassword', host='db', port= '5432')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions") #SQL query to get all the questions
    data = cursor.fetchall() #stores the questions in a variable called data
    
    #parsing the data from postgres and returning it as a json
    columns = ( 'id', 'question', 'answerA', 'answerB', 'answerC', 'answerD', 'correctAnswer')
    results = {}
    i = 1
    for row in data:
        question = dict(zip(columns, row))
        results[str(i)] = question
        i += 1
    return json.dumps(results, indent=2)

    # getting the json from a file rather than the backend
    # with open('questions.json') as f: 
    #     data = json.load(f)
    #     return data
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

