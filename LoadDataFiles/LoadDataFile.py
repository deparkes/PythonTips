# LoadDataFile.py
# Duncan Parkes

# We'll be using numpy - a numerical programming module for python
# and the csv module, for processing csv files
import numpy as np
import csv

# Using the csv module can be a quick and easy way to load data.
# The function can even load any headers which are stored as comma separated
# values.
# This is a powerful module, but here we will just simply load in the text.
csv_file = csv.reader(open('csv_module.csv', 'rb'))
# We can iterate over the object produced by this command
# Let's print out each row:
print 'csv_module.csv'
for row in csv_file:
	print row

# Although the csv module is an easy way to load csv files, for data processing
# and analysis it can be easier to use the numpy module.
# The simplest way to load data is with the loadtxt function
# We have less control over how we import that data.
# Since we know there are two lines of non-data, we skip those
data = np.loadtxt("numpy_data.csv", delimiter=',', skiprows=2)
print "numpy_data.csv, loadtxt"
print(data)

# A more advanced way to load text data is with the numpy function genfromtxt
# With this function we have more control over how we import the data.
# This time rather than ignore the column headings, we can tell python to 
# interpret the column headings.
# Our data file has two dummy comments in, which we will skip with
# skip_header=2
data2 = np.genfromtxt("numpy_data.csv", dtype=None, delimiter=',', names=True, skip_header=2)
print 'numpy_data.csv, genfromtxt\n, data file headers'
print(data2.dtype.names)
print(data2)

# We can also specify our column headings from within python, rather than 
# reading them from the file:
names = ["xdata", "y1", "y2", "y3"]
data3 = np.genfromtxt("numpy_data.csv", dtype=None, delimiter=',', names=names, skip_header=0)
print 'numpy_data.csv, genfromtxt\n, script headers'
print(data3.dtype.names)
print(data3)



			

