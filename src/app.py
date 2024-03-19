from flask import Flask, render_template, request
import pandas as pd
import search, inputCheck
app = Flask(__name__)
from exception import InputOutofOntarioError


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            if inputCheck.is_within_ontario(request.form['latitude'], request.form['longitude']):
                return search.search_coordinates()
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
