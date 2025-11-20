import csv
from datetime import datetime
import matplotlib.pyplot as pt

file_name='data/sd_weather.csv'

#get header information

with open(file_name) as f:
	reader=csv.reader(f)
	header=next(reader)
	#print("Printing Column names: ")
	#print(header)

	#get date, max and min wind speed data

	dates=[]
	max_wind=[]
	min_wind=[]

	for row in reader:
		curr_date=datetime.strptime(row[1],'%Y-%m-%d')
		date=curr_date.date()
		maxW=row[7]
		dates.append(date)
		max_wind.append(maxW)
		minW=row[9]
		min_wind.append(minW)

#plotting the data
pt.style.use('_mpl-gallery')
fig,ax=pt.subplots()
ax.plot(dates,max_wind,c='red')
ax.plot(dates,min_wind,c='blue')

#formatting the plot
pt.title('Daily Max and Min Wind Speeds')
pt.xlabel('')
pt.ylabel('Wind Speedds (mph)')
pt.show()

#print("Max Wind Speeds are: ")	
#print(max_wind)
#print("Min Wind Speeds are: ")
#print(min_wind)

# print headers and their index positions

#for index,col_header in enumerate(header):
#	print(index,col_header)
