import pandas as pd
import sqlite3, datetime


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
		ORDER BY quantity DESC, "Product Name" DESC;
	"""

	#populate a file that has the database query ran
	date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	filename = f"{date} log.csv"
	with open(filename, mode="x") as log:
		pass

	#print out details for query to the console
	for row in cur.execute(query):
		datafile = open(filename ,"a")
		datafile.write(str(row))
		datafile.write("\n")

	datafile.close()
	conn.close()

if __name__ == "__main__":
    main()

