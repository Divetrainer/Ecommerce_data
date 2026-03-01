import pandas as pd
import sqlite3

def main():

	# iniate connection to sql database in project directory
	conn = sqlite3.connect(r"/home/ipohl/workspace/github.com/Divetrainer/Ecommerce_data/ecommerce.db")

	#pull csv file into database to run sql queries against it
	ecommerce_data = pd.read_csv('ecommerce_sales_data.csv')
	ecommerce_data.to_sql('ecommerce', conn, if_exists='replace', index=False)

	#create a cursor object to run sql queries onto the database
	cur = conn.cursor()

	#query you want to execute against the data store here
	query = """
		SELECT
		"Product Name"
		, quantity as qt
		, sales
		FROM ecommerce
		WHERE sales > 1000
		AND quantity > 8
		AND ecommerce.profit > 100
		ORDER BY quantity DESC;
	"""

	for row in cur.execute(query):
		print(row)

	conn.close()

if __name__ == "__main__":
    main()
