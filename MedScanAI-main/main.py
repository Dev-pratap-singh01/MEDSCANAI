from flask import Flask, render_template, redirect, url_for
import subprocess
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Homepage with buttons to open each model

@app.route('/model1')
def model1():
    subprocess.Popen(['python', 'model1/app.py'])
    return render_template('index.html') 

# @app.route('/model2')
# def model2():
#     subprocess.Popen(['python', 'model2/app.py'])
#     return render_template('model2/model2.html')  # Renders model2's page

# @app.route('/model3')
# def model3():
#     subprocess.Popen(['python', 'model3/app.py'])
#     return render_template('model3/model3.html')  # Renders model3's page

# @app.route('/model4')
# def model4():
#     subprocess.Popen(['python', 'model4/app.py'])
#     return render_template('model4/model4.html')  # Renders model4's page

@app.route('/model5')
def model5():
    subprocess.Popen(['python', 'model5/app.py'])
    return render_template('model5/templates/index.html')  # Renders model5's page

if __name__ == "__main__":
    app.run(debug=True)
