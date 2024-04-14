requirements:
	pip install -r requirements.txt --user
database: 
	python src/database/calculation.py
app:
	python src/user/main.py
test: 
	python src/database/test_calculation.py
	python src/user/test_input_check.py
	python src/user/test_search.py
	python src/user/test_visualization.py
clean:
	rm results.csv
