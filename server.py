import os
import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/<string:page_name>')
def index(page_name=None):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except Exception:
            return "didn't save in database"
    else:
        return "something go wrong"


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'{email},{subject},{message}\n')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_write = csv.writer(database, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email, subject, message])
