import csv
with open('writeee.csv', 'r') as csvfile:
	reader=csv.reader(csvfile)
	for row in reader:
		print (row)

csvfile.close()
