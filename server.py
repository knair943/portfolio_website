from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/send_message', methods=['POST', 'GET'])
def send_message():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong try again'

# def write_to_database(data):
#     with open('database.txt', mode='a') as dbase:
#         email = data["email"]
#         name = data["name"]
#         message = data["message"]
#         file = dbase.write(f'\n{email},{name},{message}')
#     print('Write successful')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as dbase:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        csv_writer = csv.writer(dbase, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])
    print('Write successful')







