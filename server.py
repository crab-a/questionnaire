from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)
print(app)
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_name(page_name=None):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('thank you.html')
		except:
			return "did not save to database"
	else:
		return "error, try again"
def write_to_txt(data):
	with open('database.txt', 'a') as database:
			database.write('\nnew entry \n')
			for key in data:
				database.write(f'{key}: {data[key]}\n')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
			email = data["email"]
			subject = data["subject"]
			massage = data["massage"]
			csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			csv_writer.writerow([email,subject,massage])
	return 'somthing went wrong'