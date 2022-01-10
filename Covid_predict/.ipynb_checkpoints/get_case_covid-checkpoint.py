import csv

file = open('time_series_covid19_confirmed_global.csv')

csvreader = csv.reader(file)
header = []
header = next(csvreader)
# print(header)

rows = []
for row in csvreader:
        rows.append(row)
print(rows)

#
#  keyword a  b   c   d e f ...   output 
#  searchs x1 x2  x3  x4 ....     number_case_covd
#  searchs x1 x2  x3  x4 ....     number_case_covd
#  searchs x1 x2  x3  x4 ....     number_case_covd
#  searchs x1 x2  x3  x4 ....     number_case_covd
#  searchs x1 x2  x3  x4 ....     number_case_covd



#ngày hiện tại
    #   keyword a  b   c   d e f ...        output 
    #   searchs x1 x2  x3  x4 ....           predict

  



