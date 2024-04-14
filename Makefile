requirements:
	pip install -r requirements.txt --user
database: 
	python src/database/calculation.py
app:
	python src/app/main.py
test: 
	python src/database/test_calculation.py
	python src/app/test_input_check.py
	python src/app/test_search.py
	python src/app/test_visualization.py
clean:
	rm results.csv
