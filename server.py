from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')    # To simplify and make codes dynamic ()
def html_page(page_name):   
    return render_template(page_name)


# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact_Us():
#     return render_template('contact.html')


# Creating database to store data submitted by employers and writting to file

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data['message']
        file = database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a') as databasecsv:
        email = data["email"]
        subject = data["subject"]
        message = data['message']
        csv_writer = csv.writer(databasecsv, delimiter = ' ', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return'Did not save to database'

    else:
        return'Something went wrong. Try again'


