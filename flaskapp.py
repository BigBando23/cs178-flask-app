# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

'''
app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        genre = request.form['genre']
        
        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        print("First Name:", first_name, "Last Name:", last_name, "Favorite Genre:", genre)
        
        flash('User added successfully!', 'success')  # 'success' is a category; makes a green banner at the top
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_user.html')


@app.route('/display-users')
def display_users():
    # hard code a value to the users_list;
    # note that this could have been a result from an SQL query :) 
    users_list = (('John','Doe','Comedy'),('Jane', 'Doe','Drama'))
    return render_template('display_users.html', users = users_list)

@app.route('/delete-user', methods=['GET', 'POST'])
def delete_users():
    if request.method == 'POST':
        
        name = request.form['name']

        print("Name has been deleted:", name)
        
        flash('User deleted successfully!', 'warning')

        return redirect(url_for('home'))
    else:
        return render_template('delete_user.html')
# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
'''



'''
@app. route("/dashboard", methods= ["GET", "POST"])
def dashboard():
    if request.method == "POST":
#a Form submission with profile data
        username = request. form. get ("username")
        first_name = request. form.get ("first _name")
        selected_languages = request. form.getlist ("languages") # List of selected languages
# SOL query to get countries where those languages are spoken
        if selected_languages:
            country_matches = get_countries_by_languages(selected_languages)
        else:
            country_matches = []
# Save first name and selected languages to user's DynamoDB profile
        update_user_profile (username, first_name, ", "join(selected_languages))
# Re-render dashboard with results
        return render_template(
            "dashboard.html",
            success=True, 
            name=first_name, 
            languages=", "•join(selected_languages), 
            country_matches=country_matches
# GET request: show form for entering name and selecting languages.
username = request.args.get ("username")
languages = get_ languages ()
# Read from query string
# Get full list of languages from MySQL
return render_template("dashboard:html", success-False, username-username, languages=languages)
'''
#---------------------------------------------------------------
#
from flask import Flask
#from flask import render_templates
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *
app = Flask(__name__)

@app.route("/")
def index():
    #Query the top 10 countries from the MySQL
    countries = get_list_of_dictionaries()
    #Render the index page with the list of countries
    return render_template("index.html", results=countries)




# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)