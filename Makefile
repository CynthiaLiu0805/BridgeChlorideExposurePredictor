requirements:
	pip install -r requirements.txt
database: 
	python src/database/calculation.py
web: 
	cd src/web && npm install 
	cd src/web && npm run serve
test: 
	python src/database/test_calculation.py
	python src/database/test_model_input.py
clean:
	rm src/web/public/pier_high.csv
	rm src/web/public/pier_low.csv
	rm src/web/public/deck.csv
	rm -rf src/database/__pycache__
