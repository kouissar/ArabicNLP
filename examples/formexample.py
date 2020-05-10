from flask import Flask, render_template, request, flash
from examples.forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

def generate_nm(name):
    print('Goodbye ' + name)
    return 'Goodbye ' + name

@app.route('/')
def home():
    generate_nm('Rafik')
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            name = request.form.get('name')
            print('the name is: ' + name)
            email = request.form.get('email')
            print('the email is: ' + email)
            age = request.form.get('Age')
            print('the age is: ',  age)
            message = generate_nm(name)
            return render_template('success.html', name=name, email=email, age=age, msg=message)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
