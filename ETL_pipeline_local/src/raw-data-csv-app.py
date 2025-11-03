#import csv module
import csv
#chciken data roles as dictionary objects
chicken_data =[{'Name':'George' , 'Breed': 'Brahma', 'Age':'2 years', 'Size':'Very Large'}]

#define column names
column_name = ['name', 'breed', 'age', 'size']
#give csv file a name
filename ="raw-data.csv"
#setup and write data to csv file
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = column_name)
    writer.writeheader()
    writer.writerows(chicken_data)


