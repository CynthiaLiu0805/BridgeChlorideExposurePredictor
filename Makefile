requirements:
	pip install -r requirements.txt --user
database: 
	python src/database/calculation.py
app:
	python src/user/main.py
# test: 
# 	python tests/test_calculation.py
# 	python tests/test_input_check.py
# 	python tests/test_search.py
# 	python tests/test_visualization.py
clean:
	rm results.csv
