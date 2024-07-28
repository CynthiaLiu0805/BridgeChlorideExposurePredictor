requirements:
	pip install -r requirements.txt --user
database: 
	python src/database/calculation.py
app:
	python src/app/main.py
web: 
	cd src/web && npm run serve
test: 
	pytest src/database/test_calculation.py
	pytest src/database/test_model_input.py
	pytest src/app/test_input_check.py
	pytest src/app/test_search.py
	pytest src/app/test_visualization.py
clean:
	rm results.csv
