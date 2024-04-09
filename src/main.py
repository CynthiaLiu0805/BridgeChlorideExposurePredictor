from flask import Flask, render_template, request
from search import Search
from input_check import Input_check
app = Flask(__name__)
from exception import InputOutofOntarioError


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            verification = Input_check(request.form['longitude'], request.form['latitude'])
            if (verification.is_within_ontario()):
                result = Search(request.form['longitude'], request.form['latitude'])
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
