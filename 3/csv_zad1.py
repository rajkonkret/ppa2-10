# pliki csv - pliki oddzielony zankiem podziału , ;tab
# Radek,Coe,2,9.1
import csv
import pandas

# pip install pandas

row = ['Radek', 'Coe', 2, '9.1']
fileds = ['name', 'branch', 'year', 'cgpa']
with open('records.csv', 'w', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fileds)
    csvwriter.writerow(row)

data = pandas.read_csv('records.csv')
print(data)
#     name branch  year  cgpa
# 0  Radek    Coe     2   9.1
print(data.columns)
