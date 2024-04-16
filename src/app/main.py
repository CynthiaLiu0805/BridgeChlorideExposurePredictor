'''
This is the control module for the software. 
The module checks if the input is valid by using the input_check module, and update the UI accordingly.
If it is valid, it searchs the result using the search module. 
The functionality of plotting graph is achieved by calling visualization module in search module. 
'''
from flask import Flask, render_template, request
from search import Search
from input_check import Input_check
app = Flask(__name__)
from exception import InputOutofOntarioError


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            long = request.form['longitude']
            lat = request.form['latitude']
            verification = Input_check(long, lat)
            if (verification.is_within_ontario()):
                result = Search(long, lat)
                return result.search_coordinates()
            else:
                raise InputOutofOntarioError
        except InputOutofOntarioError as e:
            return render_template('index.html', warning="The input needs to be a coordinate inside Ontario.")
        except ValueError as e:
            return render_template('index.html', warning=str(e) + ". The input needs to be a coordinate inside Ontario.")
    else:
        return render_template('index.html')



if __name__ == '__main__':

    app.run(debug=True)
