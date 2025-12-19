requirements:
	pip install -r requirements.txt --user
database: 
	python src/database/calculation.py
app:
	python src/app/main.py
web: 
	cd src/web && npm install 
	cd src/web && npm run serve
test: 
	python src/database/test_calculation.py
	python src/database/test_model_input.py
clean:
	rm pier_high.csv
	rm pier_low.csv
	rm deck.csv
