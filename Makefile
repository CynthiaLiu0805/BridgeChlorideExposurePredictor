requirements:
	pip install -r requirements.txt
database: 
	python3 src/calculation.py
app:
	python3 src/main.py
clean:
	rm results.csv
