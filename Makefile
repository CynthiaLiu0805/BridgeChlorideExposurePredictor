requirements:
	pip install -r requirements.txt --user
database: 
	python src/calculation.py
app:
	python src/main.py
clean:
	rm results.csv
