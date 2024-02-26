from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_very_secret_key'  # Replace with a real secret key in production

@app.route('/')
def home():
    # Clear the session at the beginning of the survey
    session.clear()
    return render_template('form.html')

@app.route('/section1', methods=['GET', 'POST'])
def section1():
    if request.method == 'POST':
        # Potentially save data from the welcome page or clear session
        session.clear()
    return render_template('section1.html')

@app.route('/section2', methods=['GET', 'POST'])
def section2():
    if request.method == 'POST':
        # Save data from section 1
        session['pizzaFlavour'] = request.form.get('pizzaFlavour')
    return render_template('section2.html')

@app.route('/section3', methods=['GET', 'POST'])
def section3():
    if request.method == 'POST':
        # Save data from section 2
        session['laysFlavour'] = request.form.get('laysFlavour')
    return render_template('section3.html')

@app.route('/section4', methods=['GET', 'POST'])
def section4():
    if request.method == 'POST':
        # Save data from section 3
        session['nbaPlayer'] = request.form.get('nbaPlayer')
    return render_template('section4.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Save data from section 4
    session['hobbies'] = request.form.getlist('hobbies')
    # Process the complete data here
    # ...
    responses = {
        'pizza_flavour': session.get('pizzaFlavour'),
        'lays_flavour': session.get('laysFlavour'),
        'nba_player': session.get('nbaPlayer'),
        'hobbies': ', '.join(session.get('hobbies', [])),  # Join the list into a string
    }
    # Clear the session after processing
    session.clear()
    return render_template('response.html', responses=responses)

if __name__ == '__main__':
    app.run(debug=True)
