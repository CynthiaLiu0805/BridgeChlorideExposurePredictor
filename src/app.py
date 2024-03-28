from flask import Flask, render_template, request
import pandas as pd
import search
from search import Search
from inputCheck import InputCheck
app = Flask(__name__)
from exception import InputOutofOntarioError


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            verification = InputCheck(request.form['longitude'], request.form['latitude'])
            if (verification.is_within_ontario()):
                result = Search(request.form['longitude'], request.form['latitude'])

            # if inputCheck.is_within_ontario(request.form['latitude'], request.form['longitude']):
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
