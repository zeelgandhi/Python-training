import csv
csvdata=[['Name', 'age'], ['Zeel', '23']]
with open('writeee.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(csvdata)
    
csvfile.close()
