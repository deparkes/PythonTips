# LoadDataFile.py
# Duncan Parkes

# We'll be using numpy, a numerical programming module for python
import numpy as np
import csv

# The simplest way to load data is with the loadtxt function
# We have less control over how we import that data.
# Since we know there are two lines of non-data, we skip those
data = np.loadtxt("data3.csv", delimiter=',', skiprows=2)
print "data 1\n"
print(data)

# A more advanced way to load text data is with the numpy function genfromtxt
# With this function we have more control over how we import the data.
# This time rather than ignore the column headings, we can tell python to 
# interpret the column headings.
# Our data file has two dummy comments in, which we will skip with
# skip_header=2
data2 = np.genfromtxt("data3.csv", dtype=None, delimiter=',', names=True, skip_header=2)
print 'Data 2\n'
print(data2.dtype.names)
print(data2)

# We can also specify our column headings from within python, rather than 
# reading them from the file:
names = ["xdata", "y1", "y2", "y3"]
data3 = np.genfromtxt("data4.csv", dtype=None, delimiter=',', names=names, skip_header=0)
print 'Data 3\n'
print(data3.dtype.names)
print(data3)


# A final alternative to the two previous functions is the module csv, which
# allows us to import csv files.
# Notice that in this case we read in all the data as 
csv_file = csv.reader(open('data4.csv', 'rb'))
# We can iterate over the object produced by this command
# Let's print out each row:
print 'Data 4'
for row in csv_file:
	print row

# Or we could print out each element:
print 'Print each element'
for row in csv_file:
	for element in row:
		print element
			

