from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "Delhi, India",
    "salary": "Rs. 15,00,000"
}, {
    "id": 3,
    "title": "Frontend Engineer",
    "location": "Remote",
}, {
    "id": 4,
    "title": "Backend Engineer",
    "location": "San Francisco, USA",
    "salary": "$150,000"
}]


@app.route('/')
def hello_jovian():
    return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route('/jobs')
def list_jobs():
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# Youtube: 1:25:00
